import { SearchStrategyRequestTypes, ActionTypes } from './Actions';
import { isEmptyObject } from '../utils/objUtils';
import { mapSearchResponse } from '../utils/responseMappers';
import ToastAlert, { AlertSeverity } from '../models/ToastAlert';
import RequestReducer from '../requests/RequestReducer';

const StoreReducer = (state, action) => {
  switch (action.type) {
    case SearchStrategyRequestTypes.RECEIVE: {
      if (!isEmptyObject(action.payload.data)) {
        return state.set(
          'searchResults',
          mapSearchResponse(action.payload.data)
        );
      }

      return state;
    }
    case SearchStrategyRequestTypes.FAILURE: {
      const { message, trace } = action.payload.error;
      return state.set(
        'alerts',
        state.get('alerts').push(
          new ToastAlert({
            message,
            extra: trace,
            severity: AlertSeverity.ERROR,
          })
        )
      );
    }
    case ActionTypes.REMOVE_ALERT: {
      return state.deleteIn(['alerts', action.payload]);
    }
    default:
      return state;
  }
};

export default (state, action) => ({
  store: StoreReducer(state.store, action),
  requestStatuses: RequestReducer(state.requestStatuses, action),
});

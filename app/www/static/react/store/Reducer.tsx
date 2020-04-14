import { SearchStrategyRequestTypes } from './Actions';
import { isEmptyObject } from '../utils/objUtils';
import { mapSearchResponse } from '../utils/responseMappers';

export default (state, action) => {
  switch (action.type) {
    case SearchStrategyRequestTypes.RECEIVE: {
      if (!isEmptyObject(action.payload.data)) {
        return mapSearchResponse(action.payload.data);
      }

      return state;
    }
    case SearchStrategyRequestTypes.FAILURE: {
      debugger;
      return state;
    }
    default:
      return state;
  }
};

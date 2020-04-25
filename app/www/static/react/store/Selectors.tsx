import { createSelector } from 'reselect';
import { RequestStatus } from '../requests/RequestTypes';
import { SearchStrategyRequestTypes } from './Actions';

const getStore = state => state.store;
const getRequestStatuses = state => state.requestStatuses;

export const makeRequestStatusSelector = actionType =>
  createSelector(getRequestStatuses, statuses =>
    statuses.get(actionType, RequestStatus.UNINITIALIZED)
  );

export const getSearchResults = createSelector(getStore, store =>
  store.get('searchResults')
);

export const getSearchRequestStatus = makeRequestStatusSelector(
  SearchStrategyRequestTypes.REQUEST
);

import { createAction } from 'redux-actions';
import { makeRequestActionTypes } from '../requests/RequestTypes';
import {
  makeRequestActions,
  fetchMakerBuilder
} from '../requests/RequestActions';
import { searchSpreadStrategy } from '../APIClient';

export enum ActionTypes {
  ADD_ALERT,
  REMOVE_ALERT
}

export const SearchStrategyRequestTypes = makeRequestActionTypes(
  'SEARCH_STRATEGY'
);
export const SearchStrategyActions = makeRequestActions(
  SearchStrategyRequestTypes
);
export const searchStrategy = fetchMakerBuilder({
  requestActions: SearchStrategyActions,
  fetch: searchSpreadStrategy
});

export const addAlert = createAction(ActionTypes.ADD_ALERT);
export const removeAlert = createAction(ActionTypes.REMOVE_ALERT);

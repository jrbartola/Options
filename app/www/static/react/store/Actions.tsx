import { createAction } from 'redux-actions';
import { makeRequestActionTypes } from '../requests/RequestTypes';
import {
  makeRequestActions,
  fetchMakerBuilder
} from '../requests/RequestActions';
import { searchSpreadStrategy, updateEnvSettings } from '../APIClient';

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

export const UpdateSettingsRequestTypes = makeRequestActionTypes(
  'UPDATE_SETTINGS'
);
export const UpdateSettingsActions = makeRequestActions(
  UpdateSettingsRequestTypes
);
export const updateSettings = fetchMakerBuilder({
  requestActions: UpdateSettingsActions,
  fetch: updateEnvSettings
});

export const addAlert = createAction(ActionTypes.ADD_ALERT);
export const removeAlert = createAction(ActionTypes.REMOVE_ALERT);

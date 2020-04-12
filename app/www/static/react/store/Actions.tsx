import { makeRequestActionTypes } from '../requests/RequestTypes';
import {
  makeRequestActions,
  fetchMakerBuilder
} from '../requests/RequestActions';

import { searchSpreadStrategy } from '../APIClient';

export const searchStrategyRequestTypes = makeRequestActionTypes(
  'SEARCH_STRATEGY'
);
export const searchStrategyActions = makeRequestActions(
  searchStrategyRequestTypes
);
export const searchStrategy = fetchMakerBuilder({
  requestActions: searchStrategyActions,
  fetch: searchSpreadStrategy
});

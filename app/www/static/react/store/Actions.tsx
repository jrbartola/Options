import { makeRequestActionTypes } from '../requests/RequestTypes';
import {
  makeRequestActions,
  fetchMakerBuilder
} from '../requests/RequestActions';

import { searchSpreadStrategy } from '../APIClient';

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

import { List, Map } from 'immutable';

export const mapSearchResponse = ({ strategyType, results }) => {
  const searchResults = Object.keys(results).map(description => ({
    description,
    ...results[description]
  }));
  return Map({ strategyType, results: List(searchResults) });
};

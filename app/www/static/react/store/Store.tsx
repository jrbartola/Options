import { Record, List, Map } from 'immutable';
import AnalysisGraph from '../models/AnalysisGraph';

const defaults = {
  graph: new AnalysisGraph(),
  searchResults: Map({
    strategyType: null,
    results: List()
  }),
  alerts: List()
};

class Store extends Record(defaults) {}

export default Store;

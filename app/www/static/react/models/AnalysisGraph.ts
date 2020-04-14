import { Record, List } from 'immutable';

const defaults = {
  title: '',
  dataPoints: List()
};

class AnalysisGraph extends Record(defaults) {}

export default AnalysisGraph;

import { Record } from 'immutable';

const defaults = {
  filterType: null,
  comparisonOp: null,
  filterValue: null
};

class SearchFilter extends Record(defaults) {
  static empty() {
    return new SearchFilter();
  }
}

export default SearchFilter;

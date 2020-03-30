import { Record } from 'immutable';

const defaults = {
  filterType: '',
  comparisonOp: '',
  filterValue: ''
};

class SearchFilter extends Record(defaults) {
  static empty() {
    return new SearchFilter();
  }
}

export default SearchFilter;

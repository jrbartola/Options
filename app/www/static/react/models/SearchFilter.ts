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

  get isEmpty() {
    return (
      this.filterType === '' ||
      this.comparisonOp === '' ||
      this.filterValue === ''
    );
  }
}

export default SearchFilter;

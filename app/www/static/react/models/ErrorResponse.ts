import { Record, List } from 'immutable';

const defaults = {
  message: '',
  trace: ''
};

class ErrorResponse extends Record(defaults) {}

export default ErrorResponse;

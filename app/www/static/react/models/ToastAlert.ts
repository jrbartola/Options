import { Record } from 'immutable';
import { capitalize } from '../utils/stringUtils';

export enum AlertSeverity {
  INFO = 'info',
  WARNING = 'warning',
  SUCCESS = 'success',
  ERROR = 'error'
}

const defaults = {
  message: '',
  extra: null,
  severity: null
};

class ToastAlert extends Record(defaults) {
  constructor({ message, extra = null, severity = AlertSeverity.INFO }) {
    super({ message: `${capitalize(severity)}: ${message}`, extra, severity });
  }
}

export default ToastAlert;

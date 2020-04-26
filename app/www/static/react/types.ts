import { Map } from 'immutable';

import Store from './store/Store';
import { RequestStatus } from './requests/RequestTypes';

export interface Context {
  store: Store;
  requestStatuses: Map<string, RequestStatus>;
}

export interface HOCMaker {
  (...args: any[]): (Component: React.ElementType) => React.ElementType;
}

export interface HOC {
  (Component: React.ElementType): React.ElementType;
}

import { Map } from 'immutable';

const initialStatusState = Map();

export default (state = initialStatusState, { meta, payload }) => {
  if (meta && meta.requestStatuses) {
    return state.withMutations((mutable) => {
      Object.keys(meta.requestStatuses).forEach((statusAction) => {
        mutable.set(statusAction, meta.requestStatuses[statusAction]);
      });
    });
  }
  return state;
};

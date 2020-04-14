import { createAction } from 'redux-actions';

import { RequestStatus } from './RequestTypes';

export const makeRequestActions = ({ REQUEST, RECEIVE, FAILURE, RESET }) => {
  return {
    request: createAction(
      REQUEST,
      id => id,
      () => {
        return {
          requestStatuses: {
            [REQUEST]: RequestStatus.PENDING
          }
        };
      }
    ),
    receive: createAction(
      RECEIVE,
      id => id,
      () => ({
        requestStatuses: {
          [REQUEST]: RequestStatus.SUCCEEDED
        }
      })
    ),
    failure: createAction(
      FAILURE,
      id => id,
      () => ({
        requestStatuses: {
          [REQUEST]: RequestStatus.FAILED
        }
      })
    ),
    reset: createAction(
      RESET,
      id => id,
      () => ({
        requestStatuses: {
          [REQUEST]: RequestStatus.UNINITIALIZED
        }
      })
    )
  };
};

export const fetchMakerBuilder = ({ requestActions, fetch }) => (
  dispatch,
  argObj,
  payload = {}
) => {
  dispatch(requestActions.request({ payload }));
  fetch(argObj)
    .then(resp => {
      dispatch(requestActions.receive({ data: resp, payload }));
    })
    .catch(err => {
      dispatch(requestActions.failure({ error: err, payload }));
    });
};

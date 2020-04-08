export enum RequestTypes {
  REQUEST,
  RECEIVE,
  FAILURE
}

export enum RequestStatus {
  UNINITIALIZED,
  PENDING,
  SUCCEEDED,
  FAILED
}

export const makeRequestActionTypes = (requestType, namespace = '') => {
  const requestName = namespace ? `${namespace}/${requestType}` : requestType;

  return {
    REQUEST: `${requestName}_REQUESTED`,
    RECEIVE: `${requestName}_RECEIVED`,
    FAILURE: `${requestName}_FAILURE`,
    RESET: `${requestName}_RESET`
  };
};

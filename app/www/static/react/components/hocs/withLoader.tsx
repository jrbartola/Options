import * as React from 'react';
import { useDashboardContext } from '../../store/Context';
import { RequestStatus } from '../../requests/RequestTypes';
import { HOCMaker, Context } from '../../types';
import LoaderOverlay from './LoaderOverlay';
import ErrorAlert from '../lib/ErrorAlert';

export const withLoader: HOCMaker = (
  getStatus: (context: Context) => RequestStatus,
  errorMessage: string
) => (Component: React.ElementType) => {
  return (props) => {
    const [context] = useDashboardContext();
    const requestStatus = getStatus(context);

    return (
      <LoaderOverlay
        isLoading={requestStatus === RequestStatus.PENDING}
        isFailed={requestStatus === RequestStatus.FAILED}
        ErrorElement={() => <ErrorAlert message={errorMessage} />}
      >
        <Component {...props} />;
      </LoaderOverlay>
    );
  };
};

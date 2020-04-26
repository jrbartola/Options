import * as React from 'react';
import { useDashboardContext } from '../../store/Context';
import { RequestStatus } from '../../requests/RequestTypes';
import { HOCMaker, Context } from '../../types';

export const withLoader: HOCMaker = (
  getStatus: (context: Context) => RequestStatus
) => (Component: React.ElementType) => {
  return (props) => {
    const [context] = useDashboardContext();
    const requestStatus = getStatus(context);

    if (requestStatus === RequestStatus.PENDING) {
      return <div>Loading...</div>;
    }

    return <Component {...props} />;
  };
};

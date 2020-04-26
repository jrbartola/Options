import * as React from 'react';

import { Context, HOCMaker } from '../../types';
import { RequestStatus } from '../../requests/RequestTypes';
import { useDashboardContext } from '../../store/Context';
import LoaderOverlay from './LoaderOverlay';

interface LoaderHOCArgs {
  ErrorElement: React.ElementType;
}

export class LoaderDep {
  readonly fetch: (...args: any[]) => void;
  readonly getStatus: (context: Context) => RequestStatus;

  constructor(fetch, getStatus) {
    this.fetch = fetch;
    this.getStatus = getStatus;
  }
}

export const makeLoaderHOC: HOCMaker = (
  loaderDep: LoaderDep,
  { ErrorElement }: LoaderHOCArgs
) => (Component: React.ElementType) => {
  const LoaderWrapper = (props) => {
    const [context] = useDashboardContext();
    const requestStatus = loaderDep.getStatus(context);

    React.useEffect(() => {
      if (requestStatus === RequestStatus.UNINITIALIZED) {
        loaderDep.fetch();
      }
    }, [requestStatus]);

    return (
      <LoaderOverlay
        isLoading={requestStatus === RequestStatus.PENDING}
        isFailed={requestStatus === RequestStatus.FAILED}
        ErrorElement={ErrorElement}
      >
        <Component {...props} />
      </LoaderOverlay>
    );
  };

  return LoaderWrapper;
};

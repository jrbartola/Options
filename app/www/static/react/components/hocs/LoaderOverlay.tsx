import * as React from 'react';

const LoaderOverlay = ({ isLoading, isFailed, ErrorElement, children }) => {
  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (isFailed) {
    return <ErrorElement />;
  }

  return children;
};

export default LoaderOverlay;

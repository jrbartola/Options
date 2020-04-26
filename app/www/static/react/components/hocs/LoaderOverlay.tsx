import * as React from 'react';
import { CircularProgress, Grid } from '@material-ui/core';
import { useGlobalStyles } from '../../styles/globalStyles';
import CenteredContainer from '../lib/layout/CenteredContainer';

const LoaderOverlay = ({ isLoading, isFailed, ErrorElement, children }) => {
  const globalClasses = useGlobalStyles();

  if (isLoading) {
    return (
      <CenteredContainer>
        <Grid item>
          <CircularProgress />
        </Grid>
      </CenteredContainer>
    );
  }

  if (isFailed) {
    return <ErrorElement />;
  }

  return children;
};

export default LoaderOverlay;

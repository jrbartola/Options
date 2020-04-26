import * as React from 'react';
import { CircularProgress, Grid } from '@material-ui/core';
import { useGlobalStyles } from '../../styles/globalStyles';

const LoaderOverlay = ({ isLoading, isFailed, ErrorElement, children }) => {
  const globalClasses = useGlobalStyles();

  if (isLoading) {
    return (
      <div className={`${globalClasses.fullHeight} ${globalClasses.fullWidth}`}>
        <Grid
          container
          className={globalClasses.fullHeight}
          justify="center"
          alignItems="center"
          direction="column"
        >
          <Grid item>
            <CircularProgress />
          </Grid>
        </Grid>
      </div>
    );
  }

  if (isFailed) {
    return <ErrorElement />;
  }

  return children;
};

export default LoaderOverlay;

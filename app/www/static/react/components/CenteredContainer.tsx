import * as React from 'react';
import { useGlobalStyles } from '../styles/globalStyles';
import { Grid } from '@material-ui/core';

const CenteredContainer = ({ children }) => {
  const globalClasses = useGlobalStyles();

  return (
    <div className={`${globalClasses.fullHeight} ${globalClasses.fullWidth}`}>
      <Grid
        container
        className={globalClasses.fullHeight}
        justify="center"
        alignItems="center"
        direction="column"
      >
        {children}
      </Grid>
    </div>
  );
};

export default CenteredContainer;

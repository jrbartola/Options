import * as React from 'react';

import { useGlobalStyles } from '../styles/globalStyles';
import { Typography, Grid } from '@material-ui/core';
import HighlightOffIcon from '@material-ui/icons/HighlightOff';

interface ErrorAlertProps {
  message: string;
}

const ErrorAlert = ({ message }: ErrorAlertProps) => {
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
        <Grid item>
          <HighlightOffIcon />
        </Grid>
        <Grid item>
          <Typography gutterBottom>{message}</Typography>
        </Grid>
      </Grid>
    </div>
  );
};

export default ErrorAlert;

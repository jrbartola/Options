import * as React from 'react';

import { useGlobalStyles } from '../../styles/globalStyles';
import { Typography, Grid } from '@material-ui/core';
import HighlightOffIcon from '@material-ui/icons/HighlightOff';
import CenteredContainer from './layout/CenteredContainer';

interface ErrorAlertProps {
  message: string;
}

const ErrorAlert = ({ message }: ErrorAlertProps) => {
  return (
    <CenteredContainer>
      <Grid item>
        <HighlightOffIcon />
      </Grid>
      <Grid item>
        <Typography gutterBottom>{message}</Typography>
      </Grid>
    </CenteredContainer>
  );
};

export default ErrorAlert;

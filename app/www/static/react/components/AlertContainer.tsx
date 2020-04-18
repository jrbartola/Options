import * as React from 'react';
import { Snackbar, IconButton } from '@material-ui/core';
import { Alert } from '@material-ui/lab';
import { Close as CloseIcon } from '@material-ui/icons';
import { useDashboardContext } from '../store/Context';
import { removeAlert } from '../store/Actions';

// Maps errors into alerts
const AlertContainer = () => {
  const [{ alerts }, dispatch] = useDashboardContext();

  const handleClose = index => dispatch(removeAlert(index));

  return (
    <>
      <Snackbar
        anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
        open={true}
        autoHideDuration={6000}
        onClose={() => {}}
        action={
          <IconButton aria-label="close" color="inherit">
            <CloseIcon />
          </IconButton>
        }
      >
        <div>
          {alerts.map((alert, i) => (
            <Alert
              key={i}
              severity={alert.severity}
              onClose={() => handleClose(i)}
            >
              {alert.message}
            </Alert>
          ))}
        </div>
      </Snackbar>
    </>
  );
};

export default AlertContainer;

import * as React from 'react';
import { Snackbar, IconButton } from '@material-ui/core';
import { Alert, AlertTitle } from '@material-ui/lab';
import { Close as CloseIcon } from '@material-ui/icons';

// Maps errors into alerts
const AlertContainer = () => {
  const [showAlerts, setShowAlerts] = React.useState(true);

  const handleClose = () => setShowAlerts(false);

  return (
    <>
      <Snackbar
        anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
        open={showAlerts}
        autoHideDuration={6000}
        onClose={() => setShowAlerts(false)}
        action={
          <IconButton aria-label="close" color="inherit" onClick={handleClose}>
            <CloseIcon />
          </IconButton>
        }
      >
        <Alert severity="error" onClose={() => {}}>
          <AlertTitle>Error</AlertTitle>
          This is an error alert — <strong>check it out!</strong>
        </Alert>
      </Snackbar>
    </>
  );
};

export default AlertContainer;

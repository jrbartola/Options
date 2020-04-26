import * as React from 'react';
import { Snackbar, IconButton } from '@material-ui/core';
import { Close as CloseIcon } from '@material-ui/icons';

import { useDashboardContext } from '../../store/Context';
import { removeAlert } from '../../store/Actions';
import ExpandableAlert from './ExpandableAlert';

// Maps errors into alerts
const AlertContainer = () => {
  const [{ store }, dispatch] = useDashboardContext();

  const handleClose = (index) => dispatch(removeAlert(index));

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
          {store.get('alerts').map((alert, i) => (
            <ExpandableAlert
              key={i}
              alert={alert}
              onClose={() => handleClose(i)}
            />
          ))}
        </div>
      </Snackbar>
    </>
  );
};

export default AlertContainer;

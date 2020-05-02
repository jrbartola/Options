import * as React from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  Button,
  DialogActions,
  DialogContentText,
  TextField
} from '@material-ui/core';

import { useDashboardContext } from '../../../store/Context';
import { updateSettings } from '../../../store/Actions';

interface TokenDialogProps {
  isOpen: boolean;
  onClose: () => void;
}

const TokenDialog = ({ isOpen, onClose }: TokenDialogProps) => {
  const [, dispatch] = useDashboardContext();
  const inputRef = React.useRef(null);

  const onSave = () => {
    updateSettings(dispatch, {
      key: 'CLIENT_TOKEN',
      value: inputRef.current.value
    });
    onClose();
  };

  return (
    <Dialog
      open={isOpen}
      onClose={onClose}
      maxWidth="sm"
      fullWidth={true}
      aria-labelledby="token-title"
      aria-describedby="token-description"
    >
      <DialogTitle id="token-title"></DialogTitle>
      <DialogContent>
        <DialogContentText id="alert-dialog-description">
          Enter your new client token
        </DialogContentText>
        <TextField
          variant="outlined"
          inputRef={inputRef}
          rows={4}
          autoFocus
          multiline
          fullWidth
        />
      </DialogContent>
      <DialogActions>
        <Button onClick={onSave} variant="contained" color="primary">
          Save
        </Button>
        <Button onClick={onClose} color="primary">
          Cancel
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default TokenDialog;

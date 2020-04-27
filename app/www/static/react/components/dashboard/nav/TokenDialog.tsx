import * as React from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  Button,
  DialogActions,
  DialogContentText,
  TextField,
} from '@material-ui/core';

interface TokenDialogProps {
  isOpen: boolean;
  onSave: () => void;
  onClose: () => void;
}

const TokenDialog = ({ isOpen, onSave, onClose }: TokenDialogProps) => {
  return (
    <Dialog
      open={isOpen}
      onClose={onClose}
      maxWidth="md"
      fullWidth={true}
      aria-labelledby="token-title"
      aria-describedby="token-description"
    >
      <DialogTitle id="token-title"></DialogTitle>
      <DialogContent>
        <DialogContentText id="alert-dialog-description">
          Enter your new client token
        </DialogContentText>
        <TextField variant="outlined" rows={4} autoFocus multiline fullWidth />
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

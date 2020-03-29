import { makeStyles } from '@material-ui/core';

export const useGlobalStyles = makeStyles(theme => ({
  formLabel: {
    fontSize: 18,
    paddingTop: theme.spacing(1),
    marginBottom: 0
  },
  fullWidth: {
    minWidth: '100%'
  },
  noTopMargin: {
    marginTop: 0
  }
}));

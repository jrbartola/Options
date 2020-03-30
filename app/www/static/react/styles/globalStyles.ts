import { makeStyles } from '@material-ui/core';

export const useGlobalStyles = makeStyles(theme => ({
  formLabel: {
    fontSize: 18,
    paddingTop: theme.spacing(1),
    marginBottom: 0
  },
  fullWidth: {
    minWidth: '100%',
    maxWidth: '100%'
  },
  fieldText: {
    fontSize: 16
  },
  noTopMargin: {
    marginTop: 0
  },
  textCenter: {
    textAlign: 'center'
  },
  relative: {
    position: 'relative'
  }
}));

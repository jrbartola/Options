import * as React from 'react';
import {
  ExpansionPanel,
  ExpansionPanelSummary,
  Typography,
  ExpansionPanelDetails,
  makeStyles
} from '@material-ui/core';
import { Alert } from '@material-ui/lab';
import { ExpandMore as ExpandMoreIcon } from '@material-ui/icons';

const useStyles = makeStyles({
  expansionOverrides: {
    backgroundColor: 'inherit',
    boxShadow: 'none',
    '&::before': {
      display: 'none'
    }
  }
});
const ExpandableAlert = ({ alert, onClose }) => {
  const classes = useStyles();
  return (
    <Alert severity={alert.severity} onClose={onClose}>
      <ExpansionPanel className={classes.expansionOverrides}>
        <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
          <Typography>{alert.message}</Typography>
        </ExpansionPanelSummary>
        {alert.extra && (
          <ExpansionPanelDetails>
            <Typography variant="caption">
              {alert.extra.split('\n').map((line, j) => (
                <p key={j}>{line}</p>
              ))}
            </Typography>
          </ExpansionPanelDetails>
        )}
      </ExpansionPanel>
    </Alert>
  );
};

export default ExpandableAlert;

import * as React from 'react';

import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';

import RiskGraph from './RiskGraph';

const useStyles = makeStyles(theme => ({
  root: {
    margin: theme.spacing(2)
  }
}));

const AnalyzeTabContent = () => {
  const classes = useStyles();

  return (
    <section className={classes.root}>
      <Grid container spacing={3}>
        <RiskGraph />
      </Grid>
    </section>
  );
};

export default AnalyzeTabContent;

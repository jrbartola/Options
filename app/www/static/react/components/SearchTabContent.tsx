import * as React from 'react';

import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';

import SearchCard from './SearchCard';
import SearchTable from './SearchTable';

import { withContext } from './hocs/withContext';

const useStyles = makeStyles(theme => ({
  root: {
    margin: theme.spacing(2)
  }
}));

const SearchTabContent = () => {
  const classes = useStyles();

  return (
    <section className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={12} md={4}>
          <SearchCard />
        </Grid>
        <Grid item xs={12} md={8}>
          <SearchTable />
        </Grid>
      </Grid>
    </section>
  );
};

export default withContext(SearchTabContent);

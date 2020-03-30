import * as React from 'react';
import { List } from 'immutable';

import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

import SearchForm from './SearchForm';
import SearchFilter from '../models/SearchFilter';

const useStyles = makeStyles(theme => ({
  card: {
    padding: theme.spacing(2),
    paddingTop: theme.spacing(1)
  },
  cardTitle: {
    fontSize: 18,
    marginBottom: theme.spacing(2)
  },
  cardContent: {
    padding: 0
  },
  form: {
    margin: theme.spacing(1)
  }
}));

const SearchCard = () => {
  const classes = useStyles();
  const [formFields, setFormFields] = React.useState({
    symbol: '',
    selectedStrategy: '',
    optionType: null,
    filters: List([SearchFilter.empty()])
  });

  return (
    <Card className={classes.card} variant="outlined">
      <CardContent className={classes.cardContent}>
        <Typography className={classes.cardTitle} color="textSecondary">
          Find Options
        </Typography>
        <SearchForm formFields={formFields} setFormFields={setFormFields} />
      </CardContent>
      <CardActions>
        <Button variant="contained" size="small" color="primary">
          Search
        </Button>
      </CardActions>
    </Card>
  );
};

export default SearchCard;

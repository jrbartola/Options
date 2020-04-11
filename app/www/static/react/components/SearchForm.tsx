import * as React from 'react';
import {
  Grid,
  TextField,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  makeStyles,
  RadioGroup,
  FormControlLabel,
  Radio,
  FormLabel,
  Slider
} from '@material-ui/core';

import StrategyTypes from '../constants/StrategyTypes';
import OptionTypes from '../constants/OptionTypes';
import { keyToAlias } from '../utils/stringUtils';
import FilterForm from './FilterForm';
import { useGlobalStyles } from '../styles/globalStyles';

const useStyles = makeStyles(theme => ({
  form: {
    margin: theme.spacing(1)
  },
  bottomMargin: {
    marginBottom: theme.spacing(2)
  }
}));

const SearchForm = ({ formFields, setFormFields }) => {
  const globalClasses = useGlobalStyles();
  const classes = useStyles();

  const { symbol, selectedStrategy, optionType, dte } = formFields;

  const handleSymbolChange = ({ target: { value } }) => {
    // Only accept alphanumerical characters
    if (!/^[A-Za-z0-9\/]*$/g.test(value)) {
      return;
    }

    setFormFields(fields => ({
      ...fields,
      symbol: (value as string).toUpperCase()
    }));
  };

  const handleTypeChange = ({ target: { value } }) => {
    setFormFields(fields => ({ ...fields, optionType: value as string }));
  };

  return (
    <form className={classes.form} noValidate autoComplete="off">
      <Grid container spacing={1} className={classes.bottomMargin}>
        <Grid item xs={12} md={4}>
          <TextField
            size="small"
            label="Symbol"
            value={symbol}
            onChange={handleSymbolChange}
            variant="outlined"
          />
        </Grid>
        <Grid item xs={12} md={8}>
          <FormControl
            variant="outlined"
            margin="dense"
            classes={{ root: globalClasses.noTopMargin }}
            className={globalClasses.fullWidth}
          >
            <InputLabel id="strategy-label">Strategy</InputLabel>
            <Select
              labelId="strategy-label"
              label="Strategy"
              value={selectedStrategy}
              onChange={({ target: { value } }) =>
                setFormFields(fields => ({
                  ...fields,
                  selectedStrategy: value as string
                }))
              }
            >
              {Object.keys(StrategyTypes).map(strategyType => (
                <MenuItem key={strategyType} value={strategyType}>
                  {keyToAlias(strategyType)}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={12} md={6}>
          <FormControl component="fieldset">
            <FormLabel component="legend">Type</FormLabel>
            <RadioGroup
              aria-label="option-type"
              name="option-type"
              value={optionType}
              onChange={handleTypeChange}
              row
            >
              {Object.keys(OptionTypes).map(optionType => (
                <FormControlLabel
                  key={optionType}
                  value={optionType}
                  control={
                    <Radio
                      size="small"
                      disabled={selectedStrategy === StrategyTypes.IRON_CONDOR}
                    />
                  }
                  label={keyToAlias(optionType)}
                />
              ))}
            </RadioGroup>
          </FormControl>
        </Grid>
        <Grid item xs={12} md={6}>
          <FormControl component="fieldset" className={globalClasses.fullWidth}>
            <FormLabel component="legend">Days to Expiration</FormLabel>
            <Slider
              value={dte}
              onChange={(_, value) =>
                setFormFields(fields => ({ ...fields, dte: value }))
              }
              step={1}
              min={1}
              max={60}
              marks={[1, 30, 45, 60].map(i => ({ value: i, label: i }))}
              valueLabelDisplay="auto"
            />
          </FormControl>
        </Grid>
      </Grid>
      <FilterForm formFields={formFields} setFormFields={setFormFields} />
    </form>
  );
};

export default SearchForm;

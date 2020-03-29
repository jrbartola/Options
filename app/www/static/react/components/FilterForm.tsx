import * as React from 'react';
import {
  Grid,
  Select,
  FormControl,
  MenuItem,
  InputLabel
} from '@material-ui/core';

import { useGlobalStyles } from '../styles/globalStyles';
import { keyToAlias } from '../utils/stringUtils';
import FilterTypes from '../constants/FilterTypes';

const FilterForm = ({formFields, setFormFields}) => {
  const globalClasses = useGlobalStyles();
  const {filters} = formFields;

  return (
    <Grid item container xs={12}>
      <Grid item xs={4}>
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
                filters: 
              }))
            }
          >
            {Object.keys(FilterTypes).map(filterType => (
              <MenuItem key={filterType} value={filterType}>
                {keyToAlias(filterType)}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
      </Grid>
    </Grid>
  );
};

export default FilterForm;

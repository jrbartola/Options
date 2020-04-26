import * as React from 'react';
import {
  Grid,
  Select,
  FormControl,
  MenuItem,
  InputLabel,
  TextField,
  IconButton,
} from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';

import { useGlobalStyles } from '../../../styles/globalStyles';
import { keyToAlias } from '../../../utils/stringUtils';
import FilterTypes from '../../../constants/FilterTypes';
import ComparisonOps, { toReadable } from '../../../constants/ComparisonOps';

const FilterRow = ({ filter, updateFilter, canDelete, onDelete }) => {
  const globalClasses = useGlobalStyles();

  return (
    <React.Fragment>
      <Grid item xs={6}>
        <FormControl
          variant="outlined"
          margin="dense"
          classes={{ root: globalClasses.noTopMargin }}
          className={globalClasses.fullWidth}
        >
          <InputLabel id="filter-label">Filter</InputLabel>
          <Select
            labelId="filter-label"
            label="Filter"
            value={filter.filterType}
            onChange={({ target: { value } }) =>
              updateFilter('filterType', value)
            }
          >
            {Object.keys(FilterTypes).map((filterType) => (
              <MenuItem key={filterType} value={filterType}>
                {keyToAlias(filterType)}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
      </Grid>
      <Grid item xs={2}>
        <FormControl
          variant="outlined"
          margin="dense"
          classes={{ root: globalClasses.noTopMargin }}
          className={globalClasses.fullWidth}
        >
          <Select
            value={filter.comparisonOp}
            onChange={({ target: { value } }) =>
              updateFilter('comparisonOp', value)
            }
          >
            {Object.keys(ComparisonOps).map((compOp) => (
              <MenuItem key={compOp} value={compOp}>
                {toReadable(compOp)}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
      </Grid>
      <Grid item xs={3}>
        <TextField
          size="small"
          label="Value"
          value={filter.filterValue}
          onChange={({ target: { value } }) => {
            updateFilter('filterValue', value);
          }}
          variant="outlined"
        />
      </Grid>
      {canDelete && (
        <Grid item xs={1}>
          <IconButton aria-label="delete" onClick={onDelete}>
            <DeleteIcon fontSize="small" />
          </IconButton>
        </Grid>
      )}
    </React.Fragment>
  );
};

export default FilterRow;

import * as React from 'react';
import { Grid, Button } from '@material-ui/core';

import FilterRow from './FilterRow';
import { useGlobalStyles } from '../styles/globalStyles';
import SearchFilter from '../models/SearchFilter';

const FilterForm = ({ formFields, setFormFields }) => {
  const globalClasses = useGlobalStyles();
  const { filters } = formFields;

  const makeUpdateFilter = index => (field, value) => {
    setFormFields(fields => ({
      ...fields,
      filters: filters.set(index, filters.get(index).set(field, value))
    }));
  };

  const addFilter = () => {
    setFormFields(fields => ({
      ...fields,
      filters: filters.push(SearchFilter.empty())
    }));
  };

  const deleteFilter = index => {
    setFormFields(fields => ({
      ...fields,
      filters: filters.delete(index)
    }));
  };

  return (
    <Grid item container xs={12} spacing={1}>
      {filters.map((filter, i) => (
        <FilterRow
          key={i}
          filter={filter}
          updateFilter={makeUpdateFilter(i)}
          onDelete={() => deleteFilter(i)}
          canDelete={i > 0}
        />
      ))}
      <Grid item xs={12} className={globalClasses.textCenter}>
        <Button
          variant="outlined"
          size="small"
          color="primary"
          onClick={addFilter}
        >
          Add Filter
        </Button>
      </Grid>
    </Grid>
  );
};

export default FilterForm;

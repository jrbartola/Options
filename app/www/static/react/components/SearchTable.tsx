import * as React from 'react';
import {
  TableContainer,
  Paper,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  Table,
  TableCellProps,
  Typography,
  Grid
} from '@material-ui/core';
import SearchIcon from '@material-ui/icons/Search';

import { useDashboardContext } from '../store/Context';
import { useGlobalStyles } from '../styles/globalStyles';
import TableColumns from '../constants/TableColumns';

const SearchTable = () => {
  const globalClasses = useGlobalStyles();
  const [{ searchResults }] = useDashboardContext();
  const strategyType = searchResults.get('strategyType');
  const results = searchResults.get('results');

  // Empty state
  if (results.size === 0) {
    return (
      <Grid
        container
        className={globalClasses.fullHeight}
        justify="center"
        alignItems="center"
        direction="column"
      >
        <Grid item>
          <SearchIcon />
        </Grid>
        <Grid item>
          <Typography>Perform a search to analyze the results</Typography>
        </Grid>
      </Grid>
    );
  }

  return (
    <TableContainer component={Paper}>
      <Table size="small">
        <TableHead>
          <TableRow>
            {TableColumns[strategyType].map((column, i) => (
              <TableCell key={i} {...(column.headerProps as TableCellProps)}>
                {column.label}
              </TableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {results.map((spread, i) => (
            <TableRow key={i} hover className={globalClasses.pointer}>
              {TableColumns[strategyType].map((column, j) => (
                <TableCell key={j} {...(column.bodyProps as TableCellProps)}>
                  {column.getValue(spread)}
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default SearchTable;

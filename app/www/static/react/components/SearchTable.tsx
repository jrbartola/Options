import * as React from 'react';
import {
  TableContainer,
  Paper,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  Table,
  TableCellProps
} from '@material-ui/core';
import { useDashboardContext } from '../store/Context';
import { useGlobalStyles } from '../styles/globalStyles';
import TableColumns from '../constants/TableColumns';

const SearchTable = () => {
  const globalClasses = useGlobalStyles();
  const [
    {
      searchResults: { strategyType, results }
    }
  ] = useDashboardContext();

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

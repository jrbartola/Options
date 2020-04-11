import * as React from 'react';
import {
  TableContainer,
  Paper,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  Table
} from '@material-ui/core';
import { useDashboardContext } from '../context';

const SearchTable = () => {
  const [{ searchResults }] = useDashboardContext();

  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Spread</TableCell>
            <TableCell align="right">Max Profit</TableCell>
            <TableCell align="right">Max Loss</TableCell>
            <TableCell align="right">Probability Profit</TableCell>
            <TableCell align="right">Expected Profit</TableCell>
            <TableCell align="right">Credit Percent</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {searchResults.map(row => (
            <TableRow key={row.name}>
              <TableCell component="th" scope="row">
                {row.description}
              </TableCell>
              <TableCell align="right">{row.maxProfit}</TableCell>
              <TableCell align="right">{row.maxLoss}</TableCell>
              <TableCell align="right">{row.probProfit}</TableCell>
              <TableCell align="right">{row.expectedProfit}</TableCell>
              <TableCell align="right">{row.creditPercent}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default SearchTable;

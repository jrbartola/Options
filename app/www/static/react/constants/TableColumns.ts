import StrategyTypes from './StrategyTypes';

export default {
  [StrategyTypes.IRON_CONDOR]: [
    {
      label: 'Spread',
      getValue: (spread) => spread.description,
      bodyProps: { component: 'th', scope: 'row' },
    },
    {
      label: 'Max Profit',
      getValue: (spread) => spread.maxProfit,
      headerProps: { align: 'right' },
      bodyProps: { align: 'right' },
    },
    {
      label: 'Max Loss',
      getValue: (spread) => spread.maxLoss,
      headerProps: { align: 'right' },
      bodyProps: { align: 'right' },
    },
    {
      label: 'Probability Profit',
      getValue: (spread) => spread.probProfit,
      headerProps: { align: 'right' },
      bodyProps: { align: 'right' },
    },
    {
      label: 'Expected Profit',
      getValue: (spread) => spread.expectedProfit,
      headerProps: { align: 'right' },
      bodyProps: { align: 'right' },
    },
    {
      label: 'Credit Percentage',
      getValue: (spread) => spread.creditPercent,
      headerProps: { align: 'right' },
      bodyProps: { align: 'right' },
    },
  ],
  [StrategyTypes.VERTICAL_CREDIT]: [],
};

import * as React from 'react';

import { DashboardContext, DispatchContext } from '../../context';
import mainReducer from '../../reducer';

const initialContext = {
  graph: { dataPoints: [] },
  searchResults: Array(20).fill({
    description: 'AAPL 4/17 IC (50/75/100/125)',
    maxProfit: 243,
    maxLoss: 257,
    probProfit: 0.47,
    expectedProfit: -0.1,
    creditPercent: 0.49
  })
};

export const withContext = WrappedComponent => {
  return props => {
    const [context, dispatch] = React.useReducer(mainReducer, initialContext);
    return (
      <DashboardContext.Provider value={context}>
        <DispatchContext.Provider value={dispatch}>
          <WrappedComponent {...props} />
        </DispatchContext.Provider>
      </DashboardContext.Provider>
    );
  };
};

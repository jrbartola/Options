import * as React from 'react';

import { DashboardContext, DispatchContext } from '../../context';
import mainReducer from '../../reducer';

const initialContext = { graph: { dataPoints: [] } };

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

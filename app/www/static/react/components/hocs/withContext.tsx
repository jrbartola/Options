import * as React from 'react';
import { List, Map } from 'immutable';

import { DashboardContext, DispatchContext } from '../../store/Context';
import mainReducer from '../../store/Reducer';
import AnalysisGraph from '../../models/AnalysisGraph';

const initialContext = {
  graph: new AnalysisGraph(),
  searchResults: Map({
    strategyType: null,
    results: List()
  }),
  alerts: List()
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

import * as React from 'react';
import { Map } from 'immutable';

import { DashboardContext, DispatchContext } from '../../store/Context';
import mainReducer from '../../store/Reducer';
import Store from '../../store/Store';

const initialContext = { store: new Store(), requestStatuses: Map() };

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

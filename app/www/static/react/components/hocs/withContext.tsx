import * as React from 'react';

import { DashboardContext, DispatchContext } from '../../store/Context';
import mainReducer from '../../store/Reducer';
import Store from '../../store/Store';

const initialContext = new Store();

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

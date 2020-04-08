import { createContext, useContext } from 'react';

export const DashboardContext = createContext(null);
export const DispatchContext = createContext(null);

export const useDashboardContext = () => {
  const context = useContext(DashboardContext);
  const dispatch = useContext(DispatchContext);

  return [context, dispatch];
};

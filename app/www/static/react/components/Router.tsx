import * as React from 'react';
import { Switch, Route } from 'react-router-dom';

import Index from './Index';

/** App will be the main container for the entire front end **/
const App = () => (
  <Switch>
    <Route exact path="/" component={Index} />
  </Switch>
);

export default App;

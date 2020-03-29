import * as React from 'react';
import { render } from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import App from './components/Router';

render(
  // <Provider value={{}}>
  <BrowserRouter>
    <App />
  </BrowserRouter>,
  // </Provider>,
  document.getElementById('app')
);

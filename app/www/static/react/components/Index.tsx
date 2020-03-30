import * as React from 'react';
import Container from '@material-ui/core/Container';
import { createMuiTheme, ThemeProvider } from '@material-ui/core';

import BodyContent from './BodyContent';
import Navbar from './Navbar';

const theme = createMuiTheme({
  overrides: {
    // Name of the component
    MuiInputBase: {
      formControl: { fontSize: 18 }
    },
    MuiFormLabel: { root: { fontSize: 16, marginTop: 2 } },
    MuiFormControlLabel: { root: { fontSize: 16 }, label: { fontSize: 18 } },
    MuiSvgIcon: { fontSizeSmall: { fontSize: 20 } }
  }
});

const Index = () => {
  return (
    <ThemeProvider theme={theme}>
      <div>
        <Navbar />
        <Container maxWidth="xl">
          <BodyContent />
        </Container>
      </div>
    </ThemeProvider>
  );
};

export default Index;

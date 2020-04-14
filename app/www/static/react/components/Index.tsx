import * as React from 'react';
import Container from '@material-ui/core/Container';
import withWidth, { isWidthUp } from '@material-ui/core/withWidth';
import { ThemeProvider } from '@material-ui/core';

import { withContext } from './hocs/withContext';
import { desktopTheme, mobileTheme } from '../styles/themes';
import Navbar from './Navbar';
import TabContainer from './TabContainer';
import AlertContainer from './AlertContainer';

const Index = ({ width }) => {
  const isDesktop = isWidthUp('sm', width);

  return (
    <ThemeProvider theme={isDesktop ? desktopTheme : mobileTheme}>
      <div>
        <AlertContainer />
        <Navbar />
        <Container maxWidth="xl">
          <TabContainer />
        </Container>
      </div>
    </ThemeProvider>
  );
};

export default withWidth()(withContext(Index));

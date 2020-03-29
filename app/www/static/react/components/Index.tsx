import * as React from 'react';
import Container from '@material-ui/core/Container';

import BodyContent from './BodyContent';
import Navbar from './Navbar';

const Index = () => {
  return (
    <div>
      <Navbar />
      <Container maxWidth="xl">
        <BodyContent />
      </Container>
    </div>
  );
};

export default Index;

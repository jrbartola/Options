import * as React from 'react';
import { Tabs, Tab, Paper, makeStyles } from '@material-ui/core';
import SearchTabContent from './SearchTabContent';
import AnalyzeTabContent from './AnalyzeTabContent';

const TabContainer = () => {
  const [tabIndex, setTabIndex] = React.useState(0);

  return (
    <>
      <Paper>
        <Tabs
          value={tabIndex}
          textColor="primary"
          indicatorColor="primary"
          onChange={(_, newIndex) => setTabIndex(newIndex)}
        >
          <Tab label="Search" />
          <Tab label="Analyze" />
        </Tabs>
      </Paper>
      {tabIndex === 0 && <SearchTabContent />}
      {tabIndex === 1 && <AnalyzeTabContent />}
    </>
  );
};

export default TabContainer;
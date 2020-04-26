import * as React from 'react';
import CanvasJSReact from '../../../../js/canvasjs.react';

import { useDashboardContext } from '../../../store/Context';

const RiskGraph = () => {
  const [{ store }] = useDashboardContext();

  return (
    <CanvasJSReact.CanvasJSChart
      options={{
        theme: 'light2', // "light1", "dark1", "dark2"
        animationEnabled: true,
        zoomEnabled: true,
        title: {
          text: 'Iron Condor SPY 4/17',
        },
        axisY: {
          includeZero: false,
        },
        data: [
          {
            type: 'line',
            dataPoints: store.getIn(['graph', 'dataPoints'], []),
          },
        ],
      }}
    />
  );
};

export default RiskGraph;

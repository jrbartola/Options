import * as React from 'react';

import CanvasJSReact from '../../js/canvasjs.react';

const RiskGraph = () => {
  return (
    <CanvasJSReact.CanvasJSChart
      options={{
        theme: 'light2', // "light1", "dark1", "dark2"
        animationEnabled: true,
        zoomEnabled: true,
        title: {
          text: 'Iron Condor SPY 4/17'
        },
        axisY: {
          includeZero: false
        },
        data: [
          {
            type: 'line',
            dataPoints: [
              { x: 115, y: -250 },
              { x: 120, y: 0 },
              { x: 125, y: 250 },
              { x: 130, y: 250 },
              { x: 135, y: 0 },
              { x: 140, y: -250 }
            ]
          }
        ]
      }}
    />
  );
};

export default RiskGraph;

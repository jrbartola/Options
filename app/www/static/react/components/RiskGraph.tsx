import * as React from 'react';

import CanvasJSReact from '../../js/canvasjs.react';

const RiskGraph = () => {
  const generateDataPoints = noOfDps => {
    var xVal = 1,
      yVal = 100;
    var dps = [];
    for (var i = 0; i < noOfDps; i++) {
      yVal = yVal + Math.round(5 + Math.random() * (-5 - 5));
      dps.push({ x: xVal, y: yVal });
      xVal++;
    }
    return dps;
  };

  return (
    <CanvasJSReact.CanvasJSChart
      options={{
        theme: 'light2', // "light1", "dark1", "dark2"
        animationEnabled: true,
        zoomEnabled: true,
        title: {
          text: 'Try Zooming and Panning'
        },
        axisY: {
          includeZero: false
        },
        data: [
          {
            type: 'area',
            dataPoints: generateDataPoints(500)
          }
        ]
      }}
    />
  );
};

export default RiskGraph;

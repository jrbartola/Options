export const searchSpreadStrategy = ({ strategyType, symbol, ...rest }) => {
  return fetch(`/api/v1/search/strategy/${strategyType}?symbol=${symbol}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(rest)
  }).then(resp => resp.json());
};

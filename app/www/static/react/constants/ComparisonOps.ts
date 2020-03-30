export const toReadable = op => {
  switch (op) {
    case 'GT':
      return '>';
    case 'GTEQ':
      return '>=';
    case 'EQ':
      return '=';
    case 'LT':
      return '<';
    case 'LTEQ':
      return '<=';
    case 'NEQ':
      return '!=';
    default:
      return null;
  }
};

export default {
  GT: 'GT',
  GTEQ: 'GTEQ',
  EQ: 'EQ',
  LT: 'LT',
  LTEQ: 'LTEQ',
  NEQ: 'NEQ'
};

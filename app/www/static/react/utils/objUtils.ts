export const isEmptyObject = obj =>
  Object.keys(obj).length === 0 && obj.constructor === Object;

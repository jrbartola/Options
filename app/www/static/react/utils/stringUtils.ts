export const capitalize = word => {
  return word.charAt(0).toUpperCase() + word.slice(1);
};

// Maps a type key to its proper alias
export const keyToAlias = key => {
  return key
    .toLowerCase()
    .replace(/_/g, ' ')
    .split(' ')
    .reduce((acc, word) => acc + capitalize(word) + ' ', '')
    .trim();
};

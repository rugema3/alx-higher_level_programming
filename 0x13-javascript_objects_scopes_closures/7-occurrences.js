#!/usr/bin/node
/*
  This function counts the number of occurrences of 'searchElement' in the 'list' using a while loop.

  @param {Array} list - The list to search for occurrences.
  @param {any} searchElement - The element to count occurrences of.

  @returns {number} - The number of occurrences of 'searchElement' in the 'list'.
*/
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let index = 0;

  while (index < list.length) {
    if (list[index] === searchElement) {
      count++;
    }
    index++;
  }

  return count;
};

#!/usr/bin/node

/*
  This function returns the reversed version of the 'list' using a while loop.

  @param {Array} list - The list to reverse.

  @returns {Array} - The reversed version of the 'list'.
*/
exports.esrever = function (list) {
  const reversedList = [];
  let i = list.length - 1;
  while (i >= 0) {
    reversedList.push(list[i]);
    i--;
  }
  return reversedList;
};

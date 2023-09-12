#!/usr/bin/node

/*
  This function converts a number from base 10 to another base using closures.

  @param {number} base - The base to which the number should be converted.

  @returns {function} - A closure function that converts a number to the specified base.
*/
exports.converter = function (base) {
  return function convertToBase (num) {
    if (num < base) {
      return num.toString(base);
    }
    return convertToBase(Math.floor(num / base)) + (num % base).toString(base);
  };
};

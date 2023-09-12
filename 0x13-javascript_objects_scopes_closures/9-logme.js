#!/usr/bin/node

exports.logMe = (function () {
  let count = 0;

  /*
    This function prints the number of arguments already printed and the new argument value.

    @param {any} item - The argument to be printed.
  */
  return function (item) {
    console.log(`${count}: ${item}`);
    count++;
  };
})();

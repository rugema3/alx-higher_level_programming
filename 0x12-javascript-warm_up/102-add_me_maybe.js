#!/usr/bin/node
/* This module defines a function addMeMaybe that increments a number
   and calls a provided function with the incremented value. */

/* Define a function named addMeMaybe. */
const addMeMaybe = function (number, theFunction) {
  /* Increment the provided number by 1 and store the result in
     incrementedNumber. */
  const incrementedNumber = number + 1;
  /* Call the provided callback function (theFunction) with the
     incremented value as an argument. */
  theFunction(incrementedNumber);
};

/* Export the addMeMaybe function so that it can be used from outside. */
module.exports.addMeMaybe = addMeMaybe;

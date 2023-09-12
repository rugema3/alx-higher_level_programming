#!/usr/bin/node
// Import the Square class correctly with the appropriate path
const OldSquare = require('./5-square');

/*
  This class represents a Square, which is a special case of a Square
  where all sides have the same length.

  It inherits from the Square class.
*/
class Square extends OldSquare {
  /*
   * This method prints the square using the specified character 'c'.
   * If 'c' is undefined, it uses 'X' as the default character.
  */
  charPrint (c) {
    if (!c) {
      c = 'X'; // Default character is 'X'
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;

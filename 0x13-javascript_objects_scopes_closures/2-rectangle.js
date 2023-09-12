#!/usr/bin/node
/*
  This class represents a Rectangle.

  It has a constructor that takes two arguments:
  - 'w' for width
  - 'h' for height

  The constructor initializes the instance attributes 'width' and 'height'
  with the values of 'w' and 'h', respectively.
*/
class Rectangle {
  constructor (w, h) {
    /*
      Inside the constructor:
      - 'this' refers to the newly created instance of the Rectangle class.
      - 'this.width' is an instance attribute that represents the width of the rectangle.
      - 'this.height' is an instance attribute that represents the height of the rectangle.

      The constructor initializes the 'width' and 'height' attributes with the values
      passed as arguments 'w' and 'h' when creating a new Rectangle instance.
    */

    /*
      Check if 'w' and 'h' are positive integers.
      If either is not a positive integer or if either is 0, create an empty object.
      Otherwise, initialize the 'width' and 'height' attributes.
    */
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      /* Create an empty object if conditions are not met */
      this.width = undefined;
      this.height = undefined;
    }
  }
}
module.exports = Rectangle;

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
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;

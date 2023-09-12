#!/usr/bin/node

/* Import the Rectangle class correctly with the appropriate path */
const Rectangle = require('./4-rectangle');

/*
  This class represents a Square, which is a special case of a Rectangle
  where all sides have the same length.

  It inherits from the Rectangle class.
*/
class Square extends Rectangle {
  constructor (size) {
    /*
      Call the constructor of the parent class (Rectangle) using super().
      Pass 'size' as both 'width' and 'height' to initialize the Rectangle.
    */
    super(size, size);
  }
}

module.exports = Square;

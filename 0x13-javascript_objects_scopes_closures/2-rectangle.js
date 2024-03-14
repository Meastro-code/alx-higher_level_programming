#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || h=== undefined || w===undefined) {
      // Create an empty object if width or height is not positive
    //  console.log('undefined');
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;

#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // Create an empty object if width or height is not positive
      console.log('Invalid dimensions. Creating an empty rectangle.');
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      // Print the rectangle using 'X'
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      console.log('Empty rectangle.');
    }
  }
}

module.exports = Rectangle;

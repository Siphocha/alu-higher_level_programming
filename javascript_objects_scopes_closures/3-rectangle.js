#!/usr/bin/node
class Rectangle {
  // defining Class with variables using constructor
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      // basically if not an integer, cannot be used for shape.
      this.width = w;
      this.height = h;
    }
  }

  // print statement for printing out shape with the X's.
  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;

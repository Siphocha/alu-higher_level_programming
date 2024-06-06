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
}

module.exports = Rectangle;

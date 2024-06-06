#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    // rotating the X's so thhey rotate to print out the X's.
    if (this.width && this.height) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double () {
    // Thi multiplies whatever input we have for width and height by 2 each for each side, since theres two sides.
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;

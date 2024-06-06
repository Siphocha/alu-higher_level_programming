#!/usr/bin/node
// Class similar to Rectanlge because it pulls from Rectangle.
const SquareBase = require('./5-square');
// Make Class of SquareBase because pulls from original Square which pulls from Rectangle
class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;

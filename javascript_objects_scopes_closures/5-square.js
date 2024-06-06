#!/usr/bin/node
// Importing Rectangle Class because can be used for Square too.
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;

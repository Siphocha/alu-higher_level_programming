#!/usr/bin/node
// This function is complex in the sense takes number form base 10 to another base depending on user argument.
exports.converter = function (base) {
  return function convert (number) {
    return number < base ? '' + (number < 10 ? number : String.fromCharCode(number + 87)) : convert((number / base) | 0) + '' + (number % base < 10 ? number % base : String.fromCharCode(number % base + 87));
  };
};

#!/usr/bin/mode
// prints number of arguments already printed and new argument
let counter = 0;
exports.logMe = function (item) {
  console.log(`${counter}: ${item}`);
  counter++;
};

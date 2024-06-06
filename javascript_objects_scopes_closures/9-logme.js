#!/usr/bin/node
// prints number of arguments already printed and new argument
let counting = 0;
exports.logMe = function (item) {
  console.log(`${counting}: ${item}`);
  counting++;
};

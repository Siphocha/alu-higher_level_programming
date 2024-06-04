#!/usr/bin/node
// This script argues for and prints factorial numbers.
function factorial (x) {
  if (isNaN(x) || x < 0) return 1;
  if (x === 0) return 1;
  return x * factorial(x- 1);
}
console.log(factorial(parseInt(process.argv[2])));

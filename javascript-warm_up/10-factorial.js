#!/usr/bin/node
// This script argues for and prints factorial numbers.
function factorial (n) {
  if (isNaN(n) || n < 0) return 1;
  if (n === 0) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(parseInt(process.argv[2])));

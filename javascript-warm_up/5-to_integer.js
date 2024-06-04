#!/usr/bin/node
// Script that takes number argument and rejects non-number arguments
const argument1 = process.argv[2];
// Converting argument to integer to verify info
const parseInting = parseInt(argument1);

if (!isNaN(parseInting)) {
  console.log(`My number: ${parseInting}`);
} else {
  // Not an integer
  console.log('Not a number');
}

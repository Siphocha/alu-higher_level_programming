#!/usr/bin/node
// Script has two arguments that have as "is" inbetween words
const argument1 = process.argv[2];
const argument2 = process.argv[3];
// [2] & [3] because its first argument by commandline then the second command line argument.

if ((argument1 === undefined && argument2 === undefined) || argument2 === 'HBTN') {
  // prints undefined for both arguments
  console.log('undefined');
} else {
  // prints the two arguments with "is" inbetween
  console.log(argument1 + 'is' + argument2);
}
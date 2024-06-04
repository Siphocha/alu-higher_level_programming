#!/usr/bin/node
//Making a square out of Xs
const square = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < square; i++) {
    let r = '';
    // r for row
    for (let n = 0; n < square; n++) {
      r += 'X';
    }
    console.log(r);
    // prints out input number with X's as square
  }
}

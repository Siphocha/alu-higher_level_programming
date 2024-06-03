
const square = parseInt(process.argv[2]);
// defining size of square made of "x"'s.
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

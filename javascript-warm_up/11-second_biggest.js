#!/usr/bin/node
// The code finds the second integer in list of arguments.
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const maximum = Math.max(...args);
  // maximum length of argument
  const FilteredArguments = args.filter(num => num !== maximum);
  const SecondMaximum = Math.max(...FilteredArguments);
  console.log(SecondMaximum);
}

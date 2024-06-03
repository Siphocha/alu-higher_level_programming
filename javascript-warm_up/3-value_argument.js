#!/usr/bin/node
if (process.argv[2] === undefined) {
  // checked if rgument is there then if no argument passed.
  console.log('No argument');
} else {
  // if there is an argument
  console.log(process.argv[2]);
}

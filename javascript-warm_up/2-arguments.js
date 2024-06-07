#!/usr/bin/node
const args = process.argv.slice(2);
// we use system argument because taking argument from system input
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}

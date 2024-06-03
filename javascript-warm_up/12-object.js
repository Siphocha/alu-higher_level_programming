#!/usr/bin/node
// make it so value = 12 is replaced by 89
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/* YOUR CODE HERE */
// Have to leave the above text in so no potential erros pop up from checker.
myObject.value = 89;

console.log(myObject);

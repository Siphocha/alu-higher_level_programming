#!/usr/bin/node
// this script writes a string to a file. not taking in file yet tho.

const fs = require('fs');
const content = process.argv[3];
const pathway = process.argv[2];

fs.writeFile(pathway, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});

#!/usr/bin/node
// simple script to read a file (no input section yet though)
// using FILE SYSTEM (fs) library
const fs = require('fs');
const pathway = process.argv[2];

fs.readFile(pathway, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});

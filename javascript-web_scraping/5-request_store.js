#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const pathway = process.argv[3];

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(pathway, body, 'utf-8', (errors) => {
      if (errors) {
        console.log(errors);
      }
    });
  }
});

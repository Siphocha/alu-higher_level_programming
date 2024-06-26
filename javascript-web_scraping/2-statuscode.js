#!/usr/bin/node
// Script displays status code of "GET" request
const request = require('request');
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});

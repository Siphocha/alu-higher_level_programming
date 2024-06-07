#!/usr/bin/node
// This script prints the title of Star Wars where each integer has a movie title equivalent
const request = require('request');
const Episodes = process.argv[2];
const Url = `https://swapi-api.alx-tools.com/api/films/${Episodes}`;

request(Url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});

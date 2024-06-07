#!/usr/bin/node
// This script prints num of movies where "Wedge Antilles" is mentioned "his ID is 18"
const request = require('request');
const Url = process.argv[2];
const WedgeAntilles = 18;

request(Url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    const movieCount = movies.reduce((count, movie) => {
      const characters = movie.characters;
      const WedgeAntillesHere = characters.some(url => url.includes(`${WedgeAntilles}/`));
      return WedgeAntillesHere ? count + 1 : count;
    }, 0);
    console.log(movieCount);
  }
});

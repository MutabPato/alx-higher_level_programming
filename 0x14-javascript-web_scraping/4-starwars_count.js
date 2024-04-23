#!/usr/bin/node

const request = require('request');

const apiURL = process.argv[2];

request.get(apiURL, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  const data = JSON.parse(body);
  const moviesWithWedgeAntilles = data.results.filter(movie => movie.characters.find(character => character.match(/\/people\/18\/?$/)));

  console.log(moviesWithWedgeAntilles.length);
});

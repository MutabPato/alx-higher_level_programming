#!/usr/bin/node

const request = require('request');

if (process.argv.length < 2) {
  console.error('Usage: ./3-starwars_title.js movieId');
  process.exit(1);
}

const movieId = process.argv[2] - 1;

request.get('https://swapi-api.alx-tools.com/api/films/', (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.results[movieId].title);
});

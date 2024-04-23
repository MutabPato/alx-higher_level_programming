#!/usr/bin/node

const request = require('request');

if (process.argv.length < 2) {
  console.error('Usage: 0-readme.js <URL>');
  process.exit(1);
}

const URL = process.argv[2];

request.get(URL, (err, res) => {
  if (err) {
    console.error('Error: ', err);
    return;
  }
  console.log('Code: ', res.statusCode);
});

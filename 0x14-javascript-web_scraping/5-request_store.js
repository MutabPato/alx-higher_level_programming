#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const requestURL = process.argv[2];

const filePath = process.argv[3];

request.get(requestURL, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error('Error:', err);
    }
  });
});

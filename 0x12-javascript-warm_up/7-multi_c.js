#!/usr/bin/node
const { argv } = require('node:process');

let i = 0;

if (!argv[2]) {
  console.log('Missing number of occurrences');
}

while (i < argv[2]) {
  console.log('C is fun');
  i++;
}

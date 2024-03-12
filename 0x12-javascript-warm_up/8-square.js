#!/usr/bin/node
const { argv } = require('node:process');

const size = argv[2];

if (!parseInt(size)) {
  console.log('Missing size');
}

let i = 0;
let j = 0;
let row = '';

for (i = 0; i < size; i++) {
  row += 'X';
}

for (j = 0; j < size; j++) {
  console.log(row);
}

#!/usr/bin/node
const { argv } = require('node:process');

let size = argv[2];

if (!parseInt(size)) {
  console.log('Missing size');
}

let i = 0;
let j = 0;
let square = '';

while (i < size) {
  
  for (j = 0; j < size; j++) {
    square =+ 'X';
  }
  square =+ '';
  i++;
}

console.log(square);

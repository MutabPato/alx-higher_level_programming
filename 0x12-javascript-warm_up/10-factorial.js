#!/usr/bin/node

const { argv } = require('node:process');

const num = parseInt(argv[2]);

function factorial (num) {
  if (isNaN(num) || num <= 1) {
    return (1);
  }
  const result = num * factorial(num - 1);
  return (result);
}

console.log(factorial(num));

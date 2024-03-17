#!/usr/bin/node

const { argv } = require('node:process');

const args = argv.slice(2).map(arg => parseInt(arg));

if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
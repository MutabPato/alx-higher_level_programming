#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 3) {
  console.error('Usage: 1-writeme.js <file_path> "content"');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, err => {
  if (err) {
    console.error('Error writing to file:', err);
  }
});

#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Usage: ./write_file.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, (error) => {
  if (error) {
    console.error(error);
  }
});

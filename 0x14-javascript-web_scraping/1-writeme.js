#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Usage: ./write_file.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf8', (error) => {
  if (error) {
    console.error(`An error occurred while writing to the file: ${filePath}`);
    console.error(error);
  } else {
    console.log(`Successfully wrote to ${filePath}`);
  }
});

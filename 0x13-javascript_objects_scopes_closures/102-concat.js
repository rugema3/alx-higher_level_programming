#!/usr/bin/node
const fs = require('fs');

/* Get command-line arguments */
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

/* Check if all required arguments are provided */
if (!sourceFile1 || !sourceFile2 || !destinationFile) {
  console.error('Usage: ./script.js sourceFile1 sourceFile2 destinationFile');
} else {
  try {
    /* Read the content of the first source file */
    const data1 = fs.readFileSync(sourceFile1, 'utf8');

    /* Read the content of the second source file */
    const data2 = fs.readFileSync(sourceFile2, 'utf8');

    /* Concatenate the data from both source files */
    const concatenatedData = data1 + data2;

    /* Write the concatenated data to the destination file */
    fs.writeFileSync(destinationFile, concatenatedData);
  } catch (error) {
    console.error('Error:', error);
  }
}

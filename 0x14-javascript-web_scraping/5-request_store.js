#!/usr/bin/node
const fs = require('fs');
const request = require('request');

if (process.argv.length !== 4) {
  console.log('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url).pipe(fs.createWriteStream(filePath));

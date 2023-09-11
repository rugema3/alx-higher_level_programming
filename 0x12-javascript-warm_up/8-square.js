#!/usr/bin/node

const arg = process.argv[2];

const size = parseInt(arg, 10);

if (!isNaN(size)) {
  if (size > 0) {
    let i = 0;
    while (i < size) {
      const row = 'X'.repeat(size);
      console.log(row);
      i++;
    }
  } else {
    console.log('Size must be a positive integer');
  }
} else {
  console.log('Missing size');
}

#!/usr/bin/node

const arg = process.argv[2];

const x = parseInt(arg, 10);

if (!isNaN(x)) {
  let count = 0;
  while (count < x) {
    console.log('C is fun');
    count++;
  }
} else {
  console.log('Missing number of occurrences');
}

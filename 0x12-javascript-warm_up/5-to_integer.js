#!/usr/bin/node

const arg = process.argv[2];

const integerNumber = parseInt(arg, 10);

if (!isNaN(integerNumber)) {
  console.log(`My number: ${integerNumber}`);
} else {
  console.log('Not a number');
}

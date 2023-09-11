#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const arg1 = parseInt(process.argv[2], 10);
const arg2 = parseInt(process.argv[3], 10);

if (!isNaN(arg1) && !isNaN(arg2)) {
  const result = add(arg1, arg2);
  console.log(result);
} else {
  console.log('NaN');
}

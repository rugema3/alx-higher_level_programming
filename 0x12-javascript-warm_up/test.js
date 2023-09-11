#!/usr/bin/node

const args = process.argv.slice(2);

let i = 0;
while (args[i] !== undefined) {
  console.log(args[i]);
  i++;
}

if (i > 0) {
  console.log(args[0]);
} else {
  console.log('No argument');
}

#!/usr/bin/node

const args = process.argv.slice(2);

const argument1 = args[0] || 'undefined';
const argument2 = args[1] || 'undefined';

console.log(`${argument1} is ${argument2}`);

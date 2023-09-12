#!/usr/bin/node
const dict = require('./101-data').dict;

// Create an array of unique values (occurrences)
const occurrences = [...new Set(Object.values(dict))];

// Initialize the new dictionary
const newDict = {};

// Iterate through unique occurrences
for (const occurrence of occurrences) {
  // Find user IDs with the same occurrence and reverse the order
  const userList = Object.keys(dict).filter((userId) => dict[userId] === occurrence).reverse();

  // Store the user IDs under the occurrence in the new dictionary
  newDict[occurrence] = userList;
}

console.log(newDict);

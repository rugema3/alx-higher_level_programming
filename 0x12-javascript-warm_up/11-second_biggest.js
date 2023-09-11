#!/usr/bin/node

/**
 * Finds the second largest integer among the provided arguments.
 *
 * @param {array} args - An array of integer arguments.
 * @returns {number} - The second largest integer, or 0 if not found.
 */
function findSecondLargestInteger (args) {
  /* Check if there are fewer than 2 arguments */
  if (args.length < 2) {
    return 0; /* If there are not enough arguments, return 0 */
  }

  /* Convert the arguments to integers and sort them in descending order */
  const integers = args.map(arg => parseInt(arg, 10));
  const sortedIntegers = integers.sort((a, b) => b - a);

  /* Remove duplicates if any */
  const uniqueIntegers = Array.from(new Set(sortedIntegers));

  /* Check if there are at least two unique integers */
  if (uniqueIntegers.length < 2) {
    return 0; /* If there are not enough unique integers, return 0 */
  } else {
    /* The second largest integer is at index 1 (0-based index) */
    return uniqueIntegers[1];
  }
}

/* Extract command-line arguments (excluding the script name) */
const args = process.argv.slice(2);

/* Call the function to find the second largest integer */
const secondLargest = findSecondLargestInteger(args);

/* Print the result to the console */
console.log(secondLargest);

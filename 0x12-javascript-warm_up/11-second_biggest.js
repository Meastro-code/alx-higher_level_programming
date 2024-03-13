#!/usr/bin/node

/**
 * Finds the second biggest integer in the list of arguments.
 * @param {number[]} args - List of integers.
 * @returns {number} - The second biggest integer.
 */
function findSecondBiggest (args) {
  if (args.length < 2) {
    return 0;
  }

  args.sort((a, b) => b - a);
  return args[1];
}

const inputArgs = process.argv.slice(2).map(Number);
const result = findSecondBiggest(inputArgs);
console.log(result);

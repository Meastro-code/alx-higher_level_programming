#!/usr/bin/node

/**
 * Computes the factorial of a given integer recursively.
 * @param {number} n - The input integer.
 * @returns {number} - The factorial of n.
 */
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const input = parseInt(process.argv[2]);

if (isNaN(input)) {
  console.log(1);
} else {
  const result = factorial(input);
  console.log(result);
}

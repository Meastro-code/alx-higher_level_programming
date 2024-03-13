#!/usr/bin/node
// Define a function to add two integers
function add (a, b) {
  return a + b;
}

// Example usage:
const firstInteger = parseInt(process.argv[2], 10);
const secondInteger = parseInt(process.argv[3], 10);

if (isNaN(firstInteger) || isNaN(secondInteger)) {
  console.log('NaN');
} else {
  console.log(add(firstInteger, secondInteger));
}

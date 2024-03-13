#!/usr/bin/node
// Print a square using the character 'X'
function printSquare (size) {
  const num = parseInt(size, 10); // Convert the argument to an integer

  if (isNaN(num)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < num; i++) {
      console.log('X'.repeat(num));
    }
  }
}

// Example usage:
printSquare(process.argv[2]);

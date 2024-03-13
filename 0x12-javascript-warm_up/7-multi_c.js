#!/usr/bin/node
// Print "C is fun" x times based on the first argument
function printCXTimes () {
  const arg = process.argv[2]; // Get the first argument

  // Convert the argument to an integer
  const numTimes = parseInt(arg, 10);

  if (isNaN(numTimes)) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < numTimes; i++) {
      console.log('C is fun');
    }
  }
}

printCXTimes();

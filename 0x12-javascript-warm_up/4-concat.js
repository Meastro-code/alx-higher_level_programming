#!/usr/bin/node
// Print two arguments passed to the script in the specified format
function printArguments (arg1, arg2) {
  console.log(`${arg1} is ${arg2}`);
}

// Example usage:

printArguments(process.argv.slice(2)[0], process.argv.slice(2)[1]);

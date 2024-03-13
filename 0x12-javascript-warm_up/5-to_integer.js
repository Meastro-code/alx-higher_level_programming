#!/usr/bin/node
// Print the first argument converted to an integer or "Not a number"
function printConvertedNumber () {
  const arg = process.argv[2]; // Get the first argument

  // Use parseInt to convert the argument to an integer
  const convertedNumber = parseInt(arg, 10);

  if (!isNaN(convertedNumber)) {
    console.log(`My number: ${convertedNumber}`);
  } else {
    console.log('Not a number');
  }
}

printConvertedNumber();

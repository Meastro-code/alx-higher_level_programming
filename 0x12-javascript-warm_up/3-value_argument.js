#!/usr/bin/node
// Print the first argument passed to the script
function printFirstArgument () {
  const args = process.argv.slice(2); // Exclude 'node' and script filename

  if (args[0] === undefined) {
    console.log('No argument');
  } else {
    console.log(args[0]);
  }
}

printFirstArgument();

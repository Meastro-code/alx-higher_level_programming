#!/usr/bin/node

/**
 * Executes the given function 'x' times.
 * @param {number} x - Number of times to execute the function.
 * @param {Function} theFunction - The function to be executed.
 */
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = {
  callMeMoby
};

#!/usr/bin/node

/**
 * Increments a number and calls the given function.
 * @param {number} number - The number to increment.
 * @param {Function} theFunction - The function to be called.
 */
function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}

module.exports = {
  addMeMaybe
};

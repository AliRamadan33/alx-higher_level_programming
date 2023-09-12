#!/usr/bin/node
// Prints a message depending on number of arguments passed

const args = process.argv;
if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}

#!/usr/bin/node
// Prints a message depending on number of arguments passed

const args = process.argv;
const num = parseInt(args[2], 10);
if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
}

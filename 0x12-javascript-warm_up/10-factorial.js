#!/usr/bin/node
// Prints a message depending on number of arguments passed

function factorial (n) {
    if (n === 1) {
      return (1);
    }
    return (n * factorial(n - 1));
  }
  
  const args = process.argv;
  
  if (isNaN(args[2])) {
    console.log('1');
  } else {
    let num = factorial(parseInt(args[2], 10));
    console.log(num);
  }

#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n === 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const val = process.argv[2];
const n = parseInt(val);

console.log(factorial(n));

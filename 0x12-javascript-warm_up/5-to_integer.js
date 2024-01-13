#!/usr/bin/node

const nb = process.argv[2];
const val = parseInt(nb);

if (!isNaN(val)) {
  console.log(`My number: ${val}`);
} else {
  console.log('Not a number');
}

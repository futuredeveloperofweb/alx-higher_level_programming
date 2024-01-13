#!/usr/bin/node
const nb = process.argv.length - 2;
if (nb === 0) {
  console.log('No argument');
} else if (nb === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

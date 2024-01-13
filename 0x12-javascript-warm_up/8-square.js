#!/usr/bin/node

const s = process.argv[2];
const square = parseInt(s);

if (!isNaN(square)) {
  for (let i = 0; i < square; i++) {
    console.log('X'.repeat(square));
  }
} else {
  console.log('Missing size');
}

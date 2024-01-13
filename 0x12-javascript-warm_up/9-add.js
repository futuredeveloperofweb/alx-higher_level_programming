#!/usr/bin/node

function add (x, y) {
  return (x + y);
}

const val1 = process.argv[2];
const val2 = process.argv[3];
const v1 = parseInt(val1);
const v2 = parseInt(val2);

if (!isNaN(v1) && !isNaN(v2)) {
  console.log(add(v1, v2));
} else {
  console.log(NaN);
}

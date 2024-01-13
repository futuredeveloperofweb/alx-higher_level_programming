#!/usr/bin/node
const dict = require('./101-data').dict;

const n = Object.values(dict).reduce((a, val) => {
  if (!a[val]) {
    a[val] = [];
  }
  a[val].unshift(Object.keys(dict).find(key => dict[key] === val));
  return a;
}, {});

console.log(n);

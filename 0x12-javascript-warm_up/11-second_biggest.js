#!/usr/bin/node

const a = process.argv.slice(2);
const nb = a.map(arg => parseInt(arg));
const s = nb.filter(n => !isNaN(n)).sort((a, b) => b - a);
const second = s[1] || 0;

console.log(second);

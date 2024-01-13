#!/usr/bin/node
const fs = require('fs');
const x = fs.readFileSync(process.argv[2]).toString();
const y = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], x + y);

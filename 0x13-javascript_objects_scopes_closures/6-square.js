#!/usr/bin/node
const SquareP = require('./5-square');
class Square extends SquareP {
  charPrint (c = 'X') {
    const row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;

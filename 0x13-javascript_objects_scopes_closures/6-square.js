#!/usr/bin/node

const BaseSquare = require('./5-square');
module.exports = class Square extends BaseSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          c = 'X';
        }
        line += c;
      }
      console.log(line);
    }
  }
};

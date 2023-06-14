#!/usr/bin/node

const BaseSquare = require('./5-square');
module.exports = class Square extends BaseSquare {
  constructor (size) {
    super();
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let line = '';
      for (let j = 0; j < this.size; j++) {
        if (c !== undefined) {
          line += c;
        } else {
          line += 'X';
        }
      }
      console.log(line);
    }
  }
};

#!/usr/bin/node
'use strict';

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += c;
        }
        console.log(line);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;

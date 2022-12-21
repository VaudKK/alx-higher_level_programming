#!/usr/bin/node
'use strict';

let count = 0;

function logMe (item) {
  this.item = item;
}

logMe.prototype.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count += 1;
};

module.exports = logMe.prototype;

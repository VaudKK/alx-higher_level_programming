#!/usr/bin/node
'use strict';

function converter (base) {
  this.base = base;
}

converter.prototype.converter = function (number) {
  return parseInt(number, 2);
}

module.exports = converter.prototype;

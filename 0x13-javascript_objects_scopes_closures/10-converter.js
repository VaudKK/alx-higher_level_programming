#!/usr/bin/node
'use strict';

function converter (base) {
  this.base = base;
}

converter.prototype.converter = function (number) {
  return parseInt(number, converter.base);
}

module.exports = converter.prototype;

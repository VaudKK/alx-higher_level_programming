#!/usr/bin/node
'use strict';

function esrever (list) {
  this.list = list;
}

esrever.prototype.esrever = function (list) {
  return list.reverse();
};

module.exports = esrever.prototype;

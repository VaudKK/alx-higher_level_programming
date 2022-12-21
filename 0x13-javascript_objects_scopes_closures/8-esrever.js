#!/usr/bin/node
'use strict';

function esrever (list) {
  this.list = list;
}

esrever.prototype.esrever = function (list) {
  const reversedList = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList[j] = list[i];
    j++;
  }

  return reversedList;
};

module.exports = esrever.prototype;

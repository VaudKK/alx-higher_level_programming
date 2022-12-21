#!/usr/bin/node
'use strict';

const myList = require('./100-data').list;
const newList = myList.map((element, index) => index * element);

console.log(myList);
console.log(newList);

#!/usr/bin/node
'use strict';

const { argv } = require('node:process');

if (argv.length > 2) {
  if (isNaN(argv[2])) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${parseInt(argv[2], 10)}`);
  }
} else {
  console.log('Not a number');
}

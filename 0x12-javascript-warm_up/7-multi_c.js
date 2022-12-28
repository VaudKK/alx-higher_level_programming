#!/usr/bin/node
const count = process.argv[2];

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < count; index++) {
    console.log('C is fun');
  }
}

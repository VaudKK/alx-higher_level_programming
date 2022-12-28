#!/usr/bin/node
const count = process.argv[2];

if (isNaN(count)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < count; i++) {
    let line = '';
    for (let y = 0; y < count; y++) {
      line += 'X';
    }
    console.log(line);
  }
}

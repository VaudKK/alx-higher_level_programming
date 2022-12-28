#!/usr/bin/node
const input = process.argv.slice(2);

if (input.length < 2) {
  console.log(0);
} else {
  input.sort().reverse();
  console.log(input[1]);
}

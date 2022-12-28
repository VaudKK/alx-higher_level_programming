#!/usr/bin/node
const input = process.argv.slice(2);

if (input.length < 2) {
  console.log(0);
} else {
  const sorted = input.sort((a, b) => b - a);
  console.log(sorted[1]);
}

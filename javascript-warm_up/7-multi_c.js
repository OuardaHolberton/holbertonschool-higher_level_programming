#!/usr/bin/node

const arg = process.argv[2];
const num = Number.parseInt(arg, 10);

if (Number.isNaN(num)) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < num; i++) {
  console.log('C is fun');
}

#!/usr/bin/node
const { argv } = require('process');
let iter = parseInt(argv[2]);

if (isNaN(iter)) {
  console.log('Missing number of occurrences');
} else {
  while (iter > 0) {
    console.log('C is fun');
    iter--;
  }
}

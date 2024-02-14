#!/usr/bin/node
const { argv } = require('process');
let firstLar = argv[2];
let secondLar;
let val;

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    val = parseInt(argv[i]);
    if (val > firstLar) {
      secondLar = firstLar;
      firstLar = val;
    }
  }
  console.log(secondLar);
}

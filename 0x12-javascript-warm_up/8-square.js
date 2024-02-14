#!/usr/bin/node
const { argv } = require('process');
const iter = parseInt(argv[2]);

if (isNaN(iter)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < iter; i++) {
    let temp = '';
    for (let j = 0; j < iter; j++) {
      temp += 'X';
    }
    console.log(temp);
  }
}

#!/usr/bin/node
const { argv } = require('process');
const list = [];

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    list.push(parseInt(argv[i]));
  }
  console.log(list[list.length - 2]);
}

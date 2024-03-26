#!/usr/bin/node

const fs = require('fs');
const argv = require('process').argv;

fs.writeFile(argv[2], argv[3], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
});

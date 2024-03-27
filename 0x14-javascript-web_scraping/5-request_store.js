#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const fs = require('fs');

request(argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(argv[3], body, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});

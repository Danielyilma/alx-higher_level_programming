#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request.get(argv[2], (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('Code: ', response.statusCode);
  }
});

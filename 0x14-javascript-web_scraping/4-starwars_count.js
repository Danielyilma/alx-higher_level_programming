#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

let responses = null;
let count = 0;

request(argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  responses = JSON.parse(body);

  responses.results.forEach(element => {
    element.characters.forEach(elem => {
      const url = 'https://swapi-api.alx-tools.com/api/people/18/';
      if (url === elem) { count++; }
    });
  });
  console.log(count);
});

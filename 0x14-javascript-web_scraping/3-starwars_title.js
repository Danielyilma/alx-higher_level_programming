#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(JSON.parse(body).title);
});

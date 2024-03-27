#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  data.characters.forEach(link => {
    request(link, (err, response, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const data2 = JSON.parse(body);
      console.log(data2.name);
    });
  });
});

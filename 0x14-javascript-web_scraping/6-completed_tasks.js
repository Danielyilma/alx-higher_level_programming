#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const dic = {};
  const data = JSON.parse(body);
  data.forEach(element => {
    if (element.completed) { dic[element.userId] = (dic[element.userId] || 0) + 1; }
  });
  console.log(dic);
});

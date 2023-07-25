#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const fs = require('fs');

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});

#!/usr/bin/node
const process = require('process');
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  if (response.statusCode === 200) {
    fs.writeFile(fileName, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.error('Request failed with status:', response.statusCode);
  }
});

#!/usr/bin/node
const ARGV = process.argv;
const request = require('request');

request.get(ARGV[2], (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + response.statusCode);
});

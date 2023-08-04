#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const modifiedUrl = url.slice(0, -5);
const finalUrl = modifiedUrl + 'people/18';
// console.log(finalUrl);

request.get(finalUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    // console.log(data);
    console.log((data.films).length);
  } else {
    console.error('Request failed with status:', response.statusCode);
  }
});

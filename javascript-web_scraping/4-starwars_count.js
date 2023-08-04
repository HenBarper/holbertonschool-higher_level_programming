#!/usr/bin/node
const request = require('request');
const url = process.argv[2] + "/18";
console.log(url);

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.films.length);
  } else {
    console.error('Request failed with status:', response.statusCode);
  }
});

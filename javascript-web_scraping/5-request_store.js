#!/usr/bin/node
const fs = require('fs');
url = process.argv[2];
fileName = process.argv[3];
let data;

request.get(url, (err, response, body) => {
    if (err) {
      console.log(err);
    }
  
    if (response.statusCode === 200) {
      data = JSON.parse(body).results;
    } else {
      console.error('Request failed with status:', response.statusCode);
    }
  });

fs.writeFile(fileName, data, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});

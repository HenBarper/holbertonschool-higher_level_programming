#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let counter = 0;
const dictionary = {};
let user = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    for (const task of data) {
      if (user !== task.userId) {
        user = task.userId;
        counter = 0;
      }
      if (task.completed === true) {
        counter++;
      }
      if (counter !== 0) {
        dictionary[user] = counter;
      }
    }
    console.log(dictionary);
  } else {
    console.error('Request failed with status:', response.statusCode);
  }
});

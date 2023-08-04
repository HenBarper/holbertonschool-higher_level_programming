#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let counter = 0;
const dictionary = {};
let user = 1;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    for (const task of data) {
      if (user !== task.userId) {
        if (user in dictionary) {
          dictionary[user] += counter;
        } else {
          dictionary[user] = counter;
        }
        user = task.userId;
        counter = 0;
      }
      if (task.completed) {
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

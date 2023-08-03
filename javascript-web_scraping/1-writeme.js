#!/usr/bin/node
const fs = require('fs');
const ARGV = process.argv;

fs.writeFile(ARGV[2], ARGV[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});

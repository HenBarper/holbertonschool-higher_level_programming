#!/usr/bin/node
const fs = require("fs");
const ARGV = process.argv;

fs.readFile(ARGV[2], 'utf-8', (err, data) => {
    if (err) {
        console.log(err);
    }
    console.log(data);
});
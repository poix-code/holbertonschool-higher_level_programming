#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    let counter = 0;
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j].slice(-3, -1) === '18') {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});

#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const results = JSON.parse(body);
    const actors = results.characters;
    for (let i = 0; i < actors.length; i++) {
      request(actors[i], (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const results = JSON.parse(body);
          console.log(results.name);
        }
      });
    }
  }
});

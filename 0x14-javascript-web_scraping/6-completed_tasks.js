#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const dict = {};
    const task = JSON.parse(body);
    for (let i = 0; i < task.length; i++) {
      const taskId = task[i].userId;
      if (task[i].completed) {
        if (taskId in dict) {
          dict[taskId]++;
        } else {
          dict[taskId] = 1;
        }
      }
    }
    console.log(dict);
  }
});

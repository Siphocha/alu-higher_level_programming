#!/usr/bin/node
// This script completed by user id. e.g: in webapp scans who does what
const request = require('request');
const Url = process.argv[2];

request(Url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const userTaskCounts = todos.reduce((counts, todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        counts[userId] = (counts[userId] || 0) + 1;
      }
      return counts;
    }, {});

    console.log(userTaskCounts);
  }
});

#!/usr/bin/node

const request = require('request');

const apiURL = process.argv[2];

request.get(apiURL, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const todos = JSON.parse(body);

  const tasksCompletedByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (tasksCompletedByUser[todo.userId]) {
        tasksCompletedByUser[todo.userId]++;
      } else {
        tasksCompletedByUser[todo.userId] = 0;
      }
    }
  });
  console.log(tasksCompletedByUser);
});

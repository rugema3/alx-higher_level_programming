#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    let completed = {};
    todos.forEach((todo) => {
      switch (true) {
        case todo.completed && completed[todo.userId] === undefined:
          completed[todo.userId] = 1;
          break;
        case todo.completed:
          completed[todo.userId] += 1;
          break;
        default:
          break;
      }
    });
    console.log(completed);
  }
});

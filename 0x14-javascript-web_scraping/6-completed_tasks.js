#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const completed = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        completed[todo.userId] = (completed[todo.userId] || 0) + 1;
      }
    });

    console.log(JSON.stringify(completed, null, 2));
  }
});

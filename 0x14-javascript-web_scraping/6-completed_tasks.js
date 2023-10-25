#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);

    const completedTasks = tasks.reduce((completed, task) => {
      if (task.completed) {
        completed[task.userId] = (completed[task.userId] || 0) + 1;
      }
      return completed;
    }, {});

    console.log(JSON.stringify(completedTasks, null, 2));
  } else {
    console.error(`Failed to retrieve task data. Status code: ${response.statusCode}`);
  }
});

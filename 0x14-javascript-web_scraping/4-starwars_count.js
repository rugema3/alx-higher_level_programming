#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const results = JSON.parse(body).results;
    const characterId = 18; // Wedge Antilles character ID

    const count = results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith(`/${characterId}/`))
        ? count + 1
        : count;
    }, 0);

    console.log(count);
  } else {
    console.error(`Failed to retrieve film data. Status code: ${response.statusCode}`);
  }
});

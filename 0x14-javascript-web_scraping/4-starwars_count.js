#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

const characterId = 18; // Wedge Antilles character ID

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const count = films.reduce((total, film) => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        return total + 1;
      }
      return total;
    }, 0);
    console.log(count);
  } else {
    console.error(`Failed to retrieve film data. Status code: ${response.statusCode}`);
  }
});

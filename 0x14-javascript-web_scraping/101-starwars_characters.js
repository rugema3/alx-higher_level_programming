#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    // Function to retrieve and print character names
    const printCharacterNames = (urls, index = 0) => {
      if (index < urls.length) {
        request(urls[index], (characterError, characterResponse, characterBody) => {
          if (!characterError && characterResponse.statusCode === 200) {
            const character = JSON.parse(characterBody);
            console.log(character.name);
            // Recursively call to print the next character
            printCharacterNames(urls, index + 1);
          } else {
            console.error(`Failed to retrieve character data. Status code: ${characterResponse.statusCode}`);
          }
        });
      }
    };

    // Start printing character names
    printCharacterNames(characterUrls);
  } else {
    console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
  }
});

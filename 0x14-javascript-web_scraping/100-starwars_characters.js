#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./100-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + movieId, function (error, response, body) {
  if (error) {
    console.log(error);
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  characterUrls.forEach((characterUrl) => {
    request.get(characterUrl, function (characterError, characterResponse, characterBody) {
      if (characterError) {
        console.log(characterError);
      }
      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  });
});

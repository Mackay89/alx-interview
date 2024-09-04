#!/usr/bin/node

// Import the 'request' library
const request = require('request');

// Define constant with the base URL of the Star Wars API
const API_URL = 'https://swapi-api.alx-tools.com/api';

// Check if the number of command line arguments is greater than 2
if (process.argv.length > 2) {
  const filmId = process.argv[2];

  // Make a request to the film resource for the specified film ID
  request(`${API_URL}/films/${filmId}/`, (err, _, body) => {
    if (err) {
      console.error(`Error fetching film data: ${err.message}`);
      return;
    }

    try {
      // Get the characters URL from the film's response body
      const charactersURLs = JSON.parse(body).characters;

      // Create an array of Promises that resolve with the names of the characters
      const characterPromises = charactersURLs.map(url =>
        new Promise((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(`Error fetching character data: ${promiseErr.message}`);
              return;
            }

            try {
              const characterName = JSON.parse(charactersReqBody).name;
              resolve(characterName);
            } catch (parseError) {
              reject(`Error parsing character data: ${parseError.message}`);
            }
          });
        })
      );

      // Wait for all Promises to resolve and log the names of the characters, separated by new lines
      Promise.all(characterPromises)
        .then(names => console.log(names.join('\n')))
        .catch(promiseError => console.error(`Error in fetching character names: ${promiseError.message}`));

    } catch (parseError) {
      console.error(`Error parsing film data: ${parseError.message}`);
    }
  });
}

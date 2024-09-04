#!/usr/bin/node

// Import the 'request' library
import request from 'request';

// Define constant with the base URL of the Star Wars API
const API_URL = 'https://swapi-api.alx-tools.com/api';

// Check if the number of command line arguments is greater than 2
if (process.argv.length > 2) {
  const filmId = process.argv[2];

  // Make a request to the film resource for the specified film ID
  request(`${API_URL}/films/${filmId}/`, (err, _, body) => {
    // If an error occurred during the request, log the error
    if (err) {
      console.error(`Error fetching film data: ${err.message}`);
      return;
    }

    try {
      // Parse the response body to get the characters URL
      const charactersURL = JSON.parse(body).characters;

      // Create an array of Promises that resolve with the names of the characters
      const charactersName = charactersURL.map(url => new Promise((resolve, reject) => {
        // Make a request to the character resource
        request(url, (promiseErr, __, charactersReqBody) => {
          // If an error occurred during the request, reject the Promise with the error
          if (promiseErr) {
            reject(`Error fetching character data: ${promiseErr.message}`);
            return;
          }
          
          try {
            // Parse the character response body
            const characterName = JSON.parse(charactersReqBody).name;
            resolve(characterName);
          } catch (parseErr) {
            reject(`Error parsing character data: ${parseErr.message}`);
          }
        });
      }));

      // Wait for all Promises to resolve and then print the character names
      Promise.all(charactersName)
        .then(names => {
          console.log(names.join('\n'));
        })
        .catch(error => {
          console.error(`Error in fetching character names: ${error}`);
        });

    } catch (parseErr) {
      console.error(`Error parsing film data: ${parseErr.message}`);
    }
  });
}


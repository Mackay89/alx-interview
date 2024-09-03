#!/usr/bin/node

// Import the 'node-fetch' library using CommonJS syntax
const fetch = require('node-fetch');

// Define constant with the base URL of the Star Wars API
const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  const filmId = process.argv[2];

  (async () => {
    try {
      // Make a request to the film resource for the specified film ID
      const response = await fetch(`${API_URL}/films/${filmId}/`);
      const data = await response.json();
      const charactersURL = data.characters;

      // Create an array of Promises that resolve with the names of the characters
      const characterNames = await Promise.all(
        charactersURL.map(async (url) => {
          const res = await fetch(url);
          const charData = await res.json();
          return charData.name;
        })
      );

      // Log the names of the characters, separated by new lines
      console.log(characterNames.join('\n'));
    } catch (err) {
      console.error('Error:', err.message);
    }
  })();
} else {
  console.log('Please provide a film ID as a command-line argument.');
}

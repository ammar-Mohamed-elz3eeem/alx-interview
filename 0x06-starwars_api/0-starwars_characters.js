#!/usr/bin/node
const request = require('request');
const args = process.argv;

if (args.length != 3) {
  process.exit(1);
}
if (parseInt(args[2]) <= 0) {
  process.exit(1);
}

function getUrl(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (err, res, body) => {
      if (err) {
        reject(err);
      }
      resolve(res);
    });
  });
}

async function getActors(filmId) {
  const res = await getUrl(
    `https://swapi-api.alx-tools.com/api/films/${filmId}`
  );
  const resObj = JSON.parse(res.body);
  if (resObj['characters'] !== undefined) {
    getActorsRec(resObj['characters']);
  }
}

async function getActorsRec(characters) {
  if (characters.length == 0) return;
  let current = characters.shift();
  const res = await getUrl(current);
  getActorsRec(characters);
  console.log(JSON.parse(res.body)['name']);
}

getActors(args[2]);

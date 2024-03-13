// db.js
const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('./database.db', (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the database.');
});

db.run('CREATE TABLE IF NOT EXISTS accounts (name TEXT, balance REAL)');

module.exports = db;
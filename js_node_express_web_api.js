const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express();
const port = 3000;
const dbName = 'sp_to_en_color.db';
const dbTableName = 'spanish_to_english';

let db = new sqlite3.Database(dbName, (err) => {
    if (err) {
    console.error(err.message);
    res.send('An error occured when trying to connect to the database.');
    return;
    }
    console.log('Connected to the in-memory SQlite database.');
});


app.get('/', function (req, res) {
   res.send('Hello, I am a JavaScript Node Express Web API server and I will serve you data!');
});


app.get('/simple-json', function (req, res) {
    english_to_spanish_objects = [{"spanish_color": "rojo", "english_color":"red"},
                    {"spanish_color": "amarillo", "english_color":"yellow"},
                    {"spanish_color": "verde", "english_color":"green"},
                    {"spanish_color": "azul", "english_color":"blue"},
                    {"spanish_color": "rosa", "english_color":"pink"}]
    res.send(english_to_spanish_objects);
 });


 app.get('/sqlite-json', function (req, res) {

    let sqlQuery = `SELECT SPANISH_COLOR, ENGLISH_COLOR from ${dbTableName}`;
    
    db.all(sqlQuery, [], (err, rows) => {
        if (err) {
            throw err;
        }
        english_to_spanish_objects = rows.map((row) => {
            return {"spanish_color": row.SPANISH_COLOR, "english_color": row.ENGLISH_COLOR};
        });
        res.send(english_to_spanish_objects);
    });

    //db.close();
});


app.get('/paused-json', function (req, res) {
    setTimeout(function () {
        english_to_spanish_object = [{"spanish_color": "rojo", "english_color":"red"},
        {"spanish_color": "amarillo", "english_color":"yellow"},
        {"spanish_color": "verde", "english_color":"green"},
        {"spanish_color": "azul", "english_color":"blue"},
        {"spanish_color": "rosa", "english_color":"pink"}]
        
        res.send(english_to_spanish_object);
    }, 5000);
});


app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
});
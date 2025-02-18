const express = require('express');
const fetch = require('node-fetch');
const path = require('path');
require('dotenv/config');

const server = express();
const port = process.env.PORT; //change port in .env to same as Flask for bug

//Serve static files from 'templates' directory
server.use(express.static(path.join(__dirname,'/static')));

//Parse JSON bodies
server.use(express.json());

server.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'index.html'));
});

server.post('/', async (req, res) => {
    const {password} = req.body;
    console.error({password})
    try {
        const response = await fetch('http://localhost:5000/', {
            method: 'POST', //change to GET for bugs
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({password})
        });

        const data = await response.json();
        res.json(data);
    } catch (error) {
        console.error('Error communicating with Flask server:', error.message);
        res.status(500).json({success: false, message: 'Server error'});
    }
});

server.listen(port, (error) => {
    if (!error) {
        console.log(`Express server running at http://localhost:${port}`)
    } else {
        console.log("Error occurred, cannot start Express server: ", error);
    }
});
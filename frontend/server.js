const express = require('express');
const path = require('path');
const cors = require('cors');
require('dotenv/config');

const server = express();
const port = 3000;

server.use(express.json());
server.use(cors());

server.use(express.static(path.join(__dirname,'/static')));

server.get('/', (_, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'index.html'));
});

server.listen(port, (error) => {
    if (!error) {
        console.log(`Express server running at http://localhost:${port}`)
    } else {
        console.log("Error occurred, cannot start Express server: ", error);
    }
});
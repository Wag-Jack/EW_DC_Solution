const express = require('express');
const app = express();
const port = 3000;

//Test to display
app.get('/', (req, res) => {
    res.send('<hl>Hello from Express frontend!</hl><p><a href="/api">Get data from Flask</a></p>');
});

app.get('/api', async (req, res) => {
    try {
        const response = await fetch('http://localhost:5000/api');
        const data = await response.json();
        res.send(`<hl>Data from Flask: ${data.message}</hl>`);
    } catch (error) {
        res.status(500).send('Error connecting to Flask server');
    }
});

app.listen(port, () => {
    console.log('Express server running on http://localhost:3000')
});
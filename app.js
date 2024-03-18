const express = require('express');
const app = express();
app.use(express.urlencoded({ extended: false }));
app.post('/login', (req, res) => {
 console.log('insecure node.js code'); // will print to the console
});

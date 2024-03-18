const express = require('express');
const app = express();
app.use(express.urlencoded({ extended: false }));
app.post('/login', (req, res) => {
 const username = req.body.username;
 const password = req.body.password;

 if (!username || !password) {
 console.log('invalid credentials');
 return;
 }

 // validate credentials here
 if (username === 'admin' && password === '4hs30jh58gs13n7ko') {
 console.log('valid credentials');
 res.status(200).json({ success: true });
 } else {
 console.log('invalid credentials');
 res.status(200).json({ success: false });
 }
});

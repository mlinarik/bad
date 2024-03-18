app.post('/login', (req, res) => {
 const username = req.body.username;
 const password = req.body.password;

 // validate credentials here
 if (username && password) {
 console.log('valid credentials');
 } else {
 console.log('invalid credentials');
 }
});

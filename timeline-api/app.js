const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use('/static',express.static('public'));
const port = process.env.PORT || 3002;

// create application/json parser
const jsonParser = bodyParser.json()

app.get('/api/v1/',function ( req,res){
    res.sendFile(`${__dirname}/home/one-content-column.html`);
})
app.post('/api/v1/validate/',jsonParser, function (req, res) {
    let token;
    try{
        console.log(req.body);
        token = req.body.jwt;
        
    }
    catch(e){
        token = "b3334a6b93.xhjs5ndkql.b333js4d51";//10-10-10
    }
    console.log("Token Provider");
    console.log(req.body);
    console.log("-".repeat(30));
    console.log("Calling 0auth API...");
    const fetchId = TOKEN_CACHE.get(token);
    console.log("Decrypting Token...");
    if (fetchId){
        console.log("Token is Valid current user is: "+fetchId);
        const refreshedToken = Math.random().toString(16).substring(2, 12)
        +'.'+ Math.random().toString(16).substring(2, 12)
        +'.'+ Math.random().toString(16).substring(2, 12);
        console.log("Refreshing Token");
        res.send({"token":refreshedToken,"user":fetchId});
    }
    else{
        console.log("Invalid Token");
        res.send({"token":false});
    }
})

app.post('/api/v1/generate/',jsonParser, function (req, res) {
    let userId;
    try{
        console.log(req.body);
        userId = req.body.userId;
    }
    catch(e){
        userId = 101;
    }
    console.log("Token Provider");
    console.log("-".repeat(30));
    console.log("Calling 0auth API...");
    console.log("Generating token for user " + userId);
    console.log("Encrypting the Payload...");
    let token = Math.random().toString(16).substring(2, 12)
    +'.'+ Math.random().toString(16).substring(2, 12)
    +'.'+ Math.random().toString(16).substring(2, 12);
    console.log("Token: "+token+" is ready!");
    TOKEN_CACHE.set(token,userId);
    res.send({"token":token});
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
})
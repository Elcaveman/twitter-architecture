const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = process.env.PORT || 3004;

// create application/json parser
const jsonParser = bodyParser.json()

const SERVICES = {};
// Django Based
SERVICES["tweet-service"] ="http://127.0.0.1:8000/api/v1/";
SERVICES["users-service"]= "http://127.0.0.1:8001/api/v1/";
SERVICES["serch-service"]= "http://127.0.0.1:8003/api/v1/";
SERVICES["social-graph-service"]= "http://127.0.0.1:8004/api/v1/";
// Node Based
SERVICES["token-provider"]= "http://127.0.0.1:3000/api/v1/";
SERVICES["media-service"]= "http://127.0.0.1:3001/api/v1/";
SERVICES["timeline-service"]= "http://127.0.0.1:3002/api/v1/";
SERVICES["message-service"]= "http://127.0.0.1:3003/api/v1/";
SERVICES["service-discovery"]= "http://127.0.0.1:3004/api/v1/";

app.use('/static',express.static('public'));

app.get('/',function ( req,res){
    res.redirect('/api/v1/');
})

app.get('/api/v1/',function ( req,res){
    res.sendFile(`${__dirname}/home/one-content-column.html`);
})

app.get('/api/v1/services',function (req,res){
    console.log("Fetching Services...");
    console.log("Services Fetched successfuly");
    res.send(SERVICES);
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
})
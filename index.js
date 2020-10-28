const express = require('express')
const app = express()
var cmd = require('node-cmd')
const port = 8000

app.use(bodyParser.urlencoded({ extended: true }));

app.use('/',require('./WebServer/routes'));

app.set('view engine','ejs');
app.set('views','./views');

app.listen(port,function(err){
    if(err)
    {
       // console.log("Error: ",err);
        console.log(`Error in running the server: ${err}`);              
    }
    console.log(`server is running on port: ${port}`);
})

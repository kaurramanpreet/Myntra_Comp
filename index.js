const express = require('express')
const app = express()
var cmd = require('node-cmd')
const port = 8000
app.get('/', (req, res) => {
    var pyProcess = cmd.get('',
    function(data, err, stderr){
    if (!err)
        res.send(data);
    else 
        console.log("python script cmd error: " + err)
    }
);
});

app.listen(port, () => console.log(`Example app listening on port 
${port}!`))

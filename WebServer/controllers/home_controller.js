var cmd = require('node-cmd')
module.exports.home = function(req, res)
{
    return res.render('home',{
            title:"Tic_Tactics_Toe"
        });
}
module.exports.socialdistance= function(req, res)
{
    var pyProcess = cmd.get('socialdistance.py',
    function(data, err, stderr)
    {
        if (!err)
            res.send(data);
        else 
            console.log("python script cmd error: " + err)
    }
);
}
module.exports.mask= function(req, res)
{
    var pyProcess = cmd.get('mask.py',
    function(data, err, stderr)
    {
        if (!err)
            res.send(data);
        else 
            console.log("python script cmd error: " + err)
    }
);
}
module.exports.counter = function(req, res)
{
    var pyProcess = cmd.get('check.py',
    function(data, err, stderr)
    {
        if (!err)
            res.send(data);
        else 
            console.log("python script cmd error: " + err)
    }
);
}
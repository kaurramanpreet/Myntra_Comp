module.exports.home = function(req, res)
{
    return res.render('home',{
        
        });
}
module.exports.socialdistance(req,res)
{
    var pyProcess = cmd.get('',
    function(data, err, stderr)
    {
        if (!err)
            res.send(data);
        else 
            console.log("python script cmd error: " + err)
    }
);
}
module.exports.mask(req,res)
{
    var pyProcess = cmd.get('',
    function(data, err, stderr)
    {
        if (!err)
            res.send(data);
        else 
            console.log("python script cmd error: " + err)
    }
);
}
module.exports.counter(req,res)
{
    var pyProcess = cmd.get('',
    function(data, err, stderr)
    {
        if (!err)
            res.send(data);
        else 
            console.log("python script cmd error: " + err)
    }
);
}
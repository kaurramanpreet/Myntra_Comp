var cmd = require('node-cmd')
module.exports.home = function(req, res)
{
    return res.render('home',{
            title:"Tic_Tactics_Toe"
        });
}
module.exports.socialdistance= function(req, res)
{
    var pyProcess = cmd.get('script1.py',
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
module.exports.maskgif = function (req, res) {
  return res.render('demo', {
    title: "mask detection demo output",
    path: "../../distance/demo.gif",
  });
};

module.exports.socialgif = function (req, res) {
  return res.render('demo', {
    title: "social distancing output",
    path: "../../distance/social-dist.gif",
  });
};

module.exports.countergif = function (req, res) {
    return res.render('demo', {
      title: "Counter output",
      path: "../../distance/counter.gif",
    });
  };
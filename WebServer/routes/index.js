const express = require('express');

const router= express.Router();
const homeController = require('../controllers/home_controller');

router.get('/', homeController.home);
router.get('/social-distance', homeController.socaildistance);
router.get('/mask', homeController.mask);
router.get('/counter', homeController.counter);

module.exports = router;

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
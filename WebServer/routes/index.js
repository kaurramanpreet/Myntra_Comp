const express = require('express');

const router= express.Router();
const homeController = require('../controllers/home_controller');

router.get('/', homeController.home);
router.get('/social-distance', homeController.socialdistance);
router.get('/mask', homeController.mask);
router.get('/counter', homeController.counter);
router.get("/Outputs/social-dist.gif", homeController.socialgif);
router.get("/Outputs/mask.gif", homeController.maskgif);
router.get("/Outputs/counter.gif", homeController.countergif);
module.exports = router;

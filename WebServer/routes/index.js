const express = require('express');

const router= express.Router();
const homeController = require('../controllers/home_controller');

router.get('/', homeController.home);
router.get('/social-distance', homeController.socialdistance);
router.get('/mask', homeController.mask);
router.get('/counter', homeController.counter);
router.get("/distance/social-dist.gif", homeController.socialgif);
router.get("/distance/mask.gif", homeController.maskgif);
router.get("/distance/counter.gif", homeController.countergif);
module.exports = router;

import express from 'express';
import controller from '../controllers/user';
import extractJWT from '../middleware/extractJWT';

const router = express.Router();

router.post('/', controller.register);
router.post('/login', controller.login);
router.get('/me/orders', extractJWT, controller.getUserOrders);

export = router;

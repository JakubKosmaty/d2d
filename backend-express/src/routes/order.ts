import express from 'express';
import controller from '../controllers/order';
import extractJWT from '../middleware/extractJWT';

const router = express.Router();

router.post('/me', extractJWT, controller.createOrder);

export = router;

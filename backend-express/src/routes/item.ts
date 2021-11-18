import express from 'express';
import controller from '../controllers/item';
import extractJWT from '../middleware/extractJWT';

const router = express.Router();

router.get('/', extractJWT, controller.getAllItems);
router.post('/', extractJWT, controller.createItem);

export = router;

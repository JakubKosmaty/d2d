import express from 'express';
import controller from '../controllers/category';
import extractJWT from '../middleware/extractJWT';

const router = express.Router();

router.get('/', controller.getAllCategories);
router.post('/', extractJWT, controller.createCategory);

export = router;

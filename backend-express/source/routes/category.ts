import express from 'express';
import controller from '../controllers/category';

const router = express.Router();

router.get('/', controller.getAllCategories);

export = router;

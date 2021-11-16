import { NextFunction, Request, Response } from 'express';
import logging from '../config/logging';
import { getRepository } from 'typeorm';
import { Category } from '../entity/category';

const NAMESPACE = 'Category';
// /orders/me
// /users/me/orders
// /categories

const getAllCategories = async (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'Token getAllCategories.');

    const dbCategories = await getRepository(Category).find({ relations: ['items'] });

    return res.json(dbCategories);
};

export default { getAllCategories };

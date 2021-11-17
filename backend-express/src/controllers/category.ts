import { NextFunction, Request, Response } from 'express';
import logging from '../config/logging';
import { getRepository } from 'typeorm';
import { Category } from '../entity/category';

const NAMESPACE = 'Category';
// /orders/me
// /users/me/orders
// /categories

const getAllCategories = async (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'getAllCategories.');

    const dbCategories = await getRepository(Category).find({ relations: ['items'] });

    return res.json(dbCategories);
};

const createCategory = async (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'createCategory.');

    const { name } = req.body;

    const category = new Category();
    category.name = name;

    const dbCategory = await getRepository(Category).save(category);

    return res.json(dbCategory);
};

export default { getAllCategories, createCategory };

import { NextFunction, Request, Response } from 'express';
import logging from '../config/logging';
import { getRepository } from 'typeorm';
import { Item } from '../entity/item';
import { Category } from '../entity/category';

const NAMESPACE = 'Item';

const getAllItems = async (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'getAllItems.');

    const dbItems = await getRepository(Item).find();

    return res.json(dbItems);
};

const createItem = async (req: Request, res: Response, next: NextFunction) => {
    const { name, price, image_url, category_id } = req.body;

    const dbCategory = await getRepository(Category).findOne({ id: category_id });

    if (!dbCategory) {
        return res.json({ error: 'Category not found' });
    }

    const item = new Item();
    item.name = name;
    item.price = price;
    item.imageUrl = image_url;
    item.category = dbCategory;

    const dbItem = await getRepository(Item).save(item);

    return res.json(dbItem);
};

export default { getAllItems, createItem };

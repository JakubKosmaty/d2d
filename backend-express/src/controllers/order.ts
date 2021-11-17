import { NextFunction, Request, Response } from 'express';
import logging from '../config/logging';
import { getRepository } from 'typeorm';
import { Category } from '../entity/category';

const NAMESPACE = 'Order';

const createOrder = async (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'createOrder.');

    const userID = res.locals.jwt.id;

    const { address, phone, items } = req.body;

    return res.json({ add: address, phone: phone, items: items });

    // return res.json(dbCategory);
};

export default { createOrder };

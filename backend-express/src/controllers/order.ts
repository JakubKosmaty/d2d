import { NextFunction, Request, Response } from 'express';
import logging from '../config/logging';
import { getRepository } from 'typeorm';
import { Order } from '../entity/order';
import { User } from '../entity/user';
import { OrderItemLink } from '../entity/orderItemLink';
import { Item } from '../entity/item';

const NAMESPACE = 'Order';

const createOrder = async (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'createOrder.');

    const userID = res.locals.jwt.id;

    const dbUser = await getRepository(User).findOne({ id: userID });

    if (!dbUser) {
        return res.status(401).json({
            message: 'Access denied'
        });
    }

    const { address, phone, items } = req.body;

    const order = new Order();
    order.address = address;
    order.phone = phone;
    order.user = dbUser;

    const dbOrder = await getRepository(Order).save(order);

    for (let item of items) {
        const dbItem = await getRepository(Item).findOne({ id: item.item_id });

        if (!dbItem) {
            return res.json({ error: 'Item not found' });
        }

        const orderItemLink = new OrderItemLink();
        orderItemLink.quantity = item.quantity;
        orderItemLink.order = dbOrder;
        orderItemLink.item = dbItem;

        await getRepository(OrderItemLink).save(orderItemLink);
    }

    return res.json({ ok: 'Ok ADDED' });
};

export default { createOrder };

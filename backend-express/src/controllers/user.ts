import { NextFunction, Request, Response } from 'express';
import bcrypt from 'bcrypt';
import logging from '../config/logging';
import { getRepository } from 'typeorm';
import { User } from '../entity/user';
import signJWT from '../functions/signJTW';
import { Order } from '../entity/order';
import { use } from '../routes/user';

const NAMESPACE = 'User';
// /orders/me
// /users/me/orders
// /categories

const register = async (req: Request, res: Response, next: NextFunction) => {
    const { name, password, email } = req.body;

    const hash = await bcrypt.hash(password, 10);

    const user = new User();
    user.name = name;
    user.password = hash;
    user.email = email;

    const dbUser = await getRepository(User).save(user);
    return res.json(dbUser);
};

const login = async (req: Request, res: Response, next: NextFunction) => {
    const { email, password } = req.body;

    const dbUser = await getRepository(User).findOne({ email: email });

    if (!dbUser) {
        return res.status(401).json({
            message: 'Access denied'
        });
    }

    const match = await bcrypt.compare(password, dbUser.password);

    if (!match) {
        return res.status(401).json({
            message: 'Access denied'
        });
    }

    signJWT(dbUser, (_error, token) => {
        if (_error) {
            return res.status(401).json({
                message: 'Unable to Sign JWT',
                error: _error
            });
        } else if (token) {
            return res.status(200).json({
                user: dbUser,
                access_token: token
            });
        }
    });
};

const getUserOrders = async (req: Request, res: Response, next: NextFunction) => {
    const userID = res.locals.jwt.id;

    // const orders = await getRepository(Order).find({ relations: ['user'], where: { userId: userID } });

    // prettier-ignore
    const orders = await getRepository(Order)
        .createQueryBuilder('order')
        .leftJoinAndSelect('order.user', 'user')
        .where('user.id = :id', {id: userID})
        .getMany();

    return res.json(orders);
};

export default { register, login, getUserOrders };

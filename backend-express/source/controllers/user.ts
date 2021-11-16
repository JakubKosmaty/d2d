import { NextFunction, Request, Response } from 'express';
import bcryptjs from 'bcryptjs';
import logging from '../config/logging';
import { getRepository } from 'typeorm';
import { User } from '../entity/user';
import signJWT from '../functions/signJTW';

const NAMESPACE = 'User';
// /orders/me
// /users/me/orders
// /categories
const validateToken = (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'Token validated, user authorized.');

    return res.status(200).json({
        message: 'Token(s) validated'
    });
};

const register = (req: Request, res: Response, next: NextFunction) => {
    let { name, password, email } = req.body;

    bcryptjs.hash(password, 10, async (hashError, hash) => {
        if (hashError) {
            return res.status(401).json({
                message: hashError.message,
                error: hashError
            });
        }

        const user = new User();
        user.name = name;
        user.password = hash;
        user.email = email;

        const dbUser = await getRepository(User).save(user);
        return res.json(dbUser);
    });
};

const login = async (req: Request, res: Response, next: NextFunction) => {
    let { email, password } = req.body;

    const dbUser = await getRepository(User).findOne({ email: email });

    if (!dbUser) {
        return res.status(404);
    }

    bcryptjs.compare(password, dbUser.password, (error, result) => {
        if (error) {
            return res.status(401).json({
                message: 'Password Mismatch'
            });
        } else if (result) {
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
        }
    });
};

export default { validateToken, register, login };

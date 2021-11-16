import { NextFunction, Request, Response } from 'express';
import bcryptjs from 'bcryptjs';
import logging from '../config/logging';

const NAMESPACE = 'User';

const validateToken = (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'Token validated, user authorized.');

    return res.status(200).json({
        message: 'Token(s) validated'
    });
};

const register = (req: Request, res: Response, next: NextFunction) => {
    let { username, password } = req.body;

    bcryptjs.hash(password, 10, (hashError, hash) => {
        if (hashError) {
            return res.status(401).json({
                message: hashError.message,
                error: hashError
            });
        }


    });
};

const login = (req: Request, res: Response, next: NextFunction) => {
    let { username, password } = req.body;

};


export default { validateToken, register, login };

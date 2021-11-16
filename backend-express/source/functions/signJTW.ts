import jwt from 'jsonwebtoken';
import config from '../config/config';
import logging from '../config/logging';

const NAMESPACE = 'Auth';

const signJWT = (user: IUser, callback: (error: Error | null, token: string | null) => void): void => {
    logging.info(NAMESPACE, `Attempting to sign token for ${user._id}`);

    jwt.sign(
        {
            username: user.username
        },
        config.server.jwtSecret,
        {
            algorithm: 'HS256'
        },
        (error, token) => {
            if (error) {
                callback(error, null);
            } else if (token) {
                callback(null, token);
            }
        }
    );
};

export default signJWT;

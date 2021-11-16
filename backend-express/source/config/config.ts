import dotenv from 'dotenv';

dotenv.config();

const SERVER = {
    host: process.env.SERVER_HOST,
    port: process.env.SERVER_PORT,
    jwtSecret: process.env.JWT_SECRET || '123'
};

const config = {
    server: SERVER
};

export default config;

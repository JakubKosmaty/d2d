import 'reflect-metadata';

import http from 'http';
import express from 'express';
import logging from './config/logging';
import config from './config/config';
import userRoutes from './routes/user';
import categoryRoutes from './routes/category';
import orderRoutes from './routes/order';
import itemRoutes from './routes/item';
import { createConnection } from 'typeorm';
import createExampleData from './exampleData';

const NAMESPACE = 'Server';
const app = express();

createConnection().then((resp) => {
    createExampleData();
});

app.use((req, res, next) => {
    logging.info(NAMESPACE, `METHOD: [${req.method}] - URL: [${req.url}]`);

    res.on('finish', () => {
        logging.info(NAMESPACE, `METHOD: [${req.method}] - URL: [${req.url}] - STATUS: [${res.statusCode}]`);
    });

    next();
});

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization');

    if (req.method == 'OPTIONS') {
        res.header('Access-Control-Allow-Methods', 'PUT, POST, PATCH, DELETE, GET');
        return res.status(200).json({});
    }

    next();
});

app.use('/users', userRoutes);
app.use('/categories', categoryRoutes);
app.use('/orders', orderRoutes);
app.use('/items', itemRoutes);

app.use((req, res, next) => res.status(404).json({ message: 'Not found' }));

const httpServer = http.createServer(app);

httpServer.listen(config.port, () => logging.info(NAMESPACE, `Server is running on port: ${config.port}`));

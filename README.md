## Dinner-to-Door App

### Built with

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/tutorial/delete/)
- [Vue.js](https://v3.vuejs.org/)
- [Express](https://expressjs.com/)
- [TypeORM](https://typeorm.io/)

### Installation with Docker

#### Vue.js + Express(JS) + MySQL

1. Clone repository
   ```sh
   git clone https://github.com/JakubKosmaty/d2d.git
   ```
2. Change directory
   ```sh
   cd d2d
   ```
3. Run docker compose
   ```bash
   docker-compose up -d
   ```
4. Open browser
   - Frontend - http://localhost

#### Vue.js + FastApi(Python) + SQLite

1. Clone repository
   ```sh
   git clone https://github.com/JakubKosmaty/d2d.git
   ```
2. Change directory
   ```sh
   cd d2d
   ```
3. Run docker compose
   ```bash
   docker-compose up -f docker-compose-python.yml -d
   ```
4. Open browser
   - Frontend - http://localhost
   - Swagger Api - http://localhost:9000/docs

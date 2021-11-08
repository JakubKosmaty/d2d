## Dinner-to-Door App

### Built with

* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLModel](https://sqlmodel.tiangolo.com/tutorial/delete/)


### Installation

#### Docker
1. Clone repository 
    ```console
    git clone https://github.com/JakubKosmaty/d2d.git
    cd d2d
    ```
2. Run docker compose
    ```console
    docker-compose up -d
    ```

#### Bare
1. Clone repository 
    ```console
    git clone https://github.com/JakubKosmaty/d2d.git
    cd d2d
    ```
2. Install dependencies
    ```console
    pip install -r requirements.txt
    ```
3. Run uvicorn server
    ```console
   uvicorn d2d.main:app --reload
    ```
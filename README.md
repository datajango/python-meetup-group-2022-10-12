# README.md

- Anthony L. Leotta
- 2022-10-12
- fastapi_poc

## Part 1

1. Install Prerequisites
    1. Install git
    1. Install pyenv
    1. Install vscode studio
    1. Install poetry
        1. (linux or macos)
            ```
            curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
            ```
        1. (windows)
            ```
            (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
            ```
        1. poetry --version
1. Initialize Git
    ```
    git init
    ```
1. Lock Python Version
    ```
    pyenv local 3.10.5
    ```
1. Initialize Poetry
    ```
    poetry init
    ```
1. Fix python version to 3.10.5 in pyproject.toml
    ```
    [tool.poetry.dependencies]
    python = "==3.10.5"
    ```
1. Install Package Dependencies Using Poetry Package MAnager
    ```
    poetry install
    ```
1. Add a .gitignore file
1. Activate Virtual Environment
    1. (windows) source .venv/Scripts/activate
    1. poetry shell
1. Add Required Packages
    ```
    poetry add fastapi uvicorn[standard]
    poetry add -D flake8 autopep8
    ```
1. Start Server
    ```
    poetry run uvicorn backend01.main:app --reload
    ```
1. Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)
1. Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
1. Visit [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
1. Visit [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

## Part 2

1. Add startup/shutdown
    ```
    @app.on_event("startup")
    async def startup_event():
        print('startup...')


    @app.on_event("shutdown")
    def shutdown_event():
        print('shutdown...')
    ```
1. Add DBSession.py
    ```
    class DBSession():
    def __init__(self) -> None:
        self.db = 'DBCONN'

    def connect(self):
        print('db connecting')

    def close(self):
        print('db closing')
    ```
1. Add deps.py
    ```
    from backend02.dbsession import DBSession


    async def get_db():
        db = DBSession()
        try:
            yield db
        finally:
            db.close()
    ```
1. Add Depends to route
    ```
    @app.get("/")
    async def main_route(dbsession: DBSession = Depends(get_db)):
        return {
            "message": "It's Alive!",
            "db": dbsession.db
        }
    ```

1. Start Server
    ```
    poetry run uvicorn backend02.main:app --reload
    ```

## Part 3

1. [aiosqlite: Sqlite for AsyncIO](https://github.com/omnilib/aiosqlite)
1. [aiosql](https://github.com/nackjicholson/aiosql)
1. poetry add aiosqlite


1. Start Server
    ```
    poetry run uvicorn backend03.main:app --reload
    ```

## Part 4

1. refactor to use one db connection created aty startup
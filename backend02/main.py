from fastapi import FastAPI
from fastapi import Depends

from backend02.dbsession import DBSession
from backend02.deps import get_db

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print('startup...')


@app.on_event("shutdown")
def shutdown_event():
    print('shutdown...')


@app.get("/")
async def main_route(dbsession: DBSession = Depends(get_db)):
    return {
        "message": "It's Alive!",
        "db": dbsession.db
    }

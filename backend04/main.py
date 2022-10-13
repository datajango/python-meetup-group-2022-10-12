from fastapi import FastAPI, Request
from fastapi import Depends

from dbsession import DBSession
from deps import get_db

from routers.users import router as users_router

app = FastAPI()

app.include_router(users_router)


@app.on_event("startup")
async def startup_event():
    print('startup...')
    app.state.db = DBSession()
    await app.state.db.connect()


@app.on_event("shutdown")
async def shutdown_event():
    print('shutdown...')
    await app.state.db.close()


@app.get("/")
async def main_route(request: Request):

    version = await request.app.state.db.version()

    return {
        "message": "It's Alive!",
        "db": version
    }

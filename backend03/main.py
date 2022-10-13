from fastapi import FastAPI, Request
from fastapi import Depends

from dbsession import DBSession
from deps import get_db

from routers.users import router as users_router

app = FastAPI(dependencies=[Depends(get_db)])

app.include_router(users_router)


@app.on_event("startup")
async def startup_event():
    print('startup...')
    app.state.db = "DBCONN"

@app.on_event("shutdown")
def shutdown_event():
    print('shutdown...')


@app.get("/")
async def main_route(request: Request, dbsession: DBSession = Depends(get_db)):

    version = await dbsession.version()

    return {
        "message": "It's Alive!",
        "db": version,
        "db2": request.app.state.db
    }

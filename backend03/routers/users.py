from fastapi import APIRouter, Depends, Request
from dbsession import DBSession
from deps import get_db

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users(dbsession: DBSession = Depends(get_db)):
    version = await dbsession.version()

    return {
            "db": version,
            "users": [
                {
                    "username": "Rick"
                },
                {
                    "username": "Morty"
                }
            ]
    }


@router.get("/users/me", tags=["users"])
async def read_user_me(request: Request):
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str,
                    dbsession: DBSession = Depends(get_db)):
    data = await dbsession.get_user(username)
    return data


@router.post("/users/")
async def create_user(request: Request,
                      dbsession: DBSession = Depends(get_db)):
    data = await request.json()
    await dbsession.add_user(data)
    return data

from fastapi import APIRouter, Depends, HTTPException, Request
from dbsession import DBSession
from deps import get_db

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users(request: Request):
    version = await request.app.state.db.version()

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
async def read_user(request: Request, username: str):
    data = await request.app.state.db.get_user(username)
    if not data:
        raise HTTPException(status_code=422, detail="Item not found")
        # return {"error": "that users does not exist in the db"}
    return data


@router.post("/users/")
async def create_user(request: Request):
    data = await request.json()
    await request.app.state.db.add_user(data)
    return data

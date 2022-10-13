from dbsession import DBSession


async def get_db():
    db = DBSession()
    await db.connect()
    try:
        yield db
    finally:
        await db.close()


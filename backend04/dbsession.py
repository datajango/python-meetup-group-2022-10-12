from aiosqlite import connect


class DBSession():
    def __init__(self) -> None:
        pass

    async def connect(self):
        print('db connecting')
        self.db = await connect(':memory:')
        await self.create_table()

    async def version(self):
        query = "select sqlite_version();"
        cursor = await self.db.execute(query)
        row = await cursor.fetchone()
        return row

    async def create_table(self):
        # cursor = await self.db.execute('SELECT * FROM some_table')
        # row = await cursor.fetchone()
        # rows = await cursor.fetchall()

        query = "CREATE TABLE IF NOT EXISTS users ("\
                "username varchar(50) NOT NULL,"\
                "email varchar(200) NOT NULL,"\
                "password varchar(256) NOT NULL"\
                ");"
        await self.db.execute(query)
        res = self.db.commit()
        return res

    async def get_user(self, username):
        query = "select rowid, * from users "\
                "where "\
                f"username = '{username}' limit 1;"

        cursor = await self.db.execute(query)
        row = await cursor.fetchone()
        # data.update({"id": cursor.lastrowid})
        if row:
            data = {
                "rowid": row[0],
                "username": row[1],
                "password": row[2],
                "email": row[3],
            }
            return data
        else:
            None

    async def add_user(self, data):
        username = data['username']
        email = data['email']
        password = data['password']

        query = "INSERT INTO users (username,email,password)"\
                "VALUES ("\
                f"'{username}','{email}','{password}'"\
                ");"
        cursor = await self.db.execute(query)
        data.update({"id": cursor.lastrowid})
        return data

    async def close(self):
        print('db closing')
        await self.db.close()

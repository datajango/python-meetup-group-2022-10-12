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
        query = "select * from users "\
                "where "\
                f"username = '{username}' limit 1;"

        cursor = await self.db.execute(query)
        row = await cursor.fetchone()
        return row

    async def add_user(self, data):
        username = data['username']
        email = data['email']
        password = data['password']

        query = "INSERT INTO users (username,email,password)"\
                "VALUES ("\
                f"'{username}','{email}','{password}'"\
                ");"
        res = await self.db.execute(query)
        return res

    async def close(self):
        print('db closing')
        await self.db.close()

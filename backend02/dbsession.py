class DBSession():
    def __init__(self) -> None:
        self.db = 'DBCONN'

    def connect(self):
        print('db connecting')

    def close(self):
        print('db closing')

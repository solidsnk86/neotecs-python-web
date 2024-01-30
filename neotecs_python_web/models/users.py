from reflex import Model, Field

class User(Model, table=True):
    username: str
    email: str
    password: str

from ...database_config import init_db
from basemodels import BaseModel


class UserModel(BaseModel):
    def __init__(self, name="name", email="email", password="password", username="username"):
        self.name = name
        self.email = email
        self.password = password
        self.username = username

    def save_user(self):
        user = {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "username": self.username

        }

        connect = init_db()
        cur = connect.cursor()

        if BaseModel().check_exist('users', 'email', self.email) == True:
            return "user already exists"

        query = """ INSERT INTO users (name, username, email, password )VALUES\
            ( %(name)s, %(username)s, %(email)s, %(password)s )RETURNING user_id """
        cur.execute(query, user)
        user_id = cur.fetchone()[0]
        connect.commit()
        connect.close()
        return user_id

    def get_username_password(self):
        pass
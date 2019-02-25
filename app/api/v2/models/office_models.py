from app.database_config import init_db
from .basemodels import BaseModel


class OfficeModel(BaseModel):
    def __init__(self, name="name", type="type", user="user"):
        
        self.name = name
        self.type = type
        self.user = user

    def save(self):
        office = {
            "name": self.name,
            "type": self.type,
            "user": self.user
        }

        connect = init_db()
        cur = connect.cursor()
        if BaseModel().check_if_item_exists('offices', 'name', self.name) == True:
            return "office already exists"

        query = """ INSERT INTO offices(type, name)VALUES\
                ( %(type)s, %(name)s) RETURNING office_id """

        cur.execute(query, office)
        type = cur.fetchone()[0]
        connect.commit()
        connect.close()
        return type


    def get_offices(self):
        connect = init_db()
        cur = connect.cursor()
        query = "SELECT type, name, user FROM offices;"
        cur.execute(query)
        data = cur.fetchall()
        res = []

        for i, items in enumerate(data):
            type, user, name = items
        offices = dict(
            user=user,
            type=type,
            name=str(name)
        )
        res.append(offices)
        return res


    def get_single_office(self, office_id):
        connect = init_db()
        cur = connect.cursor()
        if BaseModel().check_if_item_exists('offices', 'office_id', office_id) == False:
            return 404

        query = "SELECT name, user, type FROM offices WHERE office_id={}".format(office_id)
        cur.execute(query)
        data = cur.fetchall()[0]
        res = []

        offices = dict(
            name=data[0],
            user=data[1],
            type=str(data[2])
        )
        res.append(offices)
        return res

    


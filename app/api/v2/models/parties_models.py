# from app.database_config import init_db
# from .basemodels import BaseModel


# class PartiesModel(BaseModel):
#     def __init__(self, name="name", type="type", user="user"):
        
#         self.name = name
#         self.type = type
#         self.user = user

#     def save(self):
#         office = {
#             "name": self.name,
#             "type": self.type,
#             "user": self.user
#         }

#         connect = init_db()
#         cur = connect.cursor()
#         if BaseModel().check_if_item_exists('offices', 'office', self.type) == True:
#             return "vote already exists"

#         query = """ INSERT INTO offices(type, name, user)VALUES\
#                 ( %(type)s, %(name)s, %(user)s, RETURNING vote_id """

#         cur.execute(query, office)
#         type = cur.fetchone()[0]
#         connect.commit()
#         connect.close()
#         return type


#     def get_single_office(self, office_id):
#         connect = init_db()
#         cur = connect.cursor()
#         if BaseModel().check_if_item_exists('offices', 'office_id', office_id) == False:
#             return 404

#         query = "SELECT type, created_on FROM offices WHERE office_id={};".format(office_id)
#         cur.execute(query)
#         data = cur.fetchall()
#         res = []

#         offices = dict(
#             name=data[0],
#             user=int(data[1]),
#             type=str(data[2])
#         )
#         res.append(offices)
#         return res

    


from app.database_config import init_db
from .basemodels import BaseModel


class PartiesModel(BaseModel):
    def __init__(self, hqAddress="hqAddress", name="name", logourl="logourl"):

        self.name = name
        self.logourl = logourl
        self.hqAddress = hqAddress

    def save(self):
        party = {
            "name": self.name,
            "logourl": self.logourl,
            "hqAddress": self.hqAddress
        }

        connect = init_db()
        cur = connect.cursor()
        if BaseModel().check_if_item_exists('parties', 'name', self.name) == True:
            return "party already exists"

        query = """ INSERT INTO parties(logourl, name, hqAddress)VALUES\
                ( %(logourl)s, %(name)s, %(hqAddress)s) RETURNING party_id """

        cur.execute(query, party)
        name = cur.fetchone()[0]
        connect.commit()
        connect.close()
        return name

    def get_parties(self):
        connect = init_db()
        cur = connect.cursor()
        query = "SELECT hqAddress, name, logourl FROM parties;"
        cur.execute(query)
        data = cur.fetchall()
        res = []

        for i, items in enumerate(data):
            logourl, hqAddress, name = items
        parties = dict(

            logourl=logourl,
            hqAddress=hqAddress,
            name=str(name)
        )
        res.append(parties)
        return res

    def get_single_party(self, party_id):
        connect = init_db()
        cur = connect.cursor()
        if BaseModel().check_if_item_exists('parties', 'party_id', party_id) == False:
            return 404

        query = "SELECT name, logourl, created_on FROM parties WHERE party_id={};".format(
            party_id)
        cur.execute(query)
        data = cur.fetchall()[0]
        res = []

        party = dict(
            name=data[0],
            hqAddress=data[1],
            logourl=str(data[2])
        )
        res.append(party)
        return res

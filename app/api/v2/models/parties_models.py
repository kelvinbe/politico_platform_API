from app.database_config import init_db

class Party:
    """ The party model """

    def __init__(self):
        self.db = init_db()

    def create_party(self, name, hqAddress, logoUrl):
        """ Create a party method """
        party = {
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl
        }
        self.db.insert('parties', party)
        return party

    def get_all_parties(self):
        """ Get all parties method """
        data = self.db.fetch_all_items('parties')
        parties = []
        for i, items in enumerate(data):
            id, name, hqaddress, logourl, dateCreated = items
            party = dict(
                id=int(id),
                name=name,
                hqaddress=hqaddress,
                logourl=logourl,
                dateCreated=dateCreated
            )
            parties.append(party)
        return parties

    def get_specific_party(self, id):
        """ Get all parties method """
        data = self.db.search_by_id('parties', id)
        for i, items in enumerate(data):
            id, name, hqAddress, logourl, dateCreated = items
            party = dict(
                id=int(id),
                name=name,
                hqAddress=hqAddress,
                logourl=logourl,
                dateCreated=dateCreated
            )
            return party

    def edit_party(self, id, name, data):
        """Update the details of a political party"""
        party = Party().get_specific_party(id)
        if Party().get_specific_party(id):
            if data.get('name') and data.get(
                    'hqAddress') and data.get('logoUrl'):
                self.db.cursor.execute(
                    "UPDATE parties SET name=%s, hqAddress=%s, logoUrl=%s WHERE id={}".format(
                        id, name), (data.get('name'), data.get('hqAddress'), data.get('logoUrl')))
                return self.db.connection.commit()

    def delete_party(self, id):
        """This function deletes a product entry in the database"""
        self.db.delete('parties', id)

    def search(self, name):
        """ This function returns True if a party name exists in the database."""
        if self.db.search_by_name('parties', name):
            return True
from app.api.v2.database.database_config import Connection


class Office:
    """ The office model """

    def __init__(self):
        self.db = Connection()

    def create_office(self, name, type):
        """ Create a office method """
        office = {
            "name": name,
            "type": type
        }
        self.db.insert('offices', office)
        return office

    def get_all_offices(self):
        """ Get all offices method """
        data = self.db.fetch_all_items('offices')
        offices = []
        for i, items in enumerate(data):
            id, officeType, name, dateCreated = items
            office = dict(
                id=int(id),
                officeType=officeType,
                name=name,
                dateCreated=dateCreated
            )
            offices.append(office)
        return offices

    def get_specific_office(self, id):
        """ Get specific office method """
        data = self.db.search_by_id('offices', id)
        for i, items in enumerate(data):
            id, officeType, name, dateCreated = items
            office = dict(
                id=int(id),
                name=name,
                officeType=officeType,
                dateCreated=dateCreated
            )
            return office

    def search(self, name):
        """ This function returns True if an office name already exists in the database."""
        if self.db.search_by_name('offices', name):
            return True
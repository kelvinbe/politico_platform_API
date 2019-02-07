parties = []
offices = []

# PartyModels


class PartyModels():

    def __init__(self):
        """Initialization."""

        self.db = parties

    def create(self, name, hqAddress, logoUrl):

        party = {
            "id": len(self.db)+1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl,
        }
        self.db.append(party)
        return party

     # Get all parties
    def get_parties(self):
        return self.db

    # Get specific Party

    def get_party(self, id):
        for party in self.db:
            if party["id"] == id:
                return party

     # Edit specific party

    def edit_party(self, id, data):
        for party in self.db:
            if party["id"] == id:
                name = data.get("name")
                hqAddress = data.get("hqAddress")
                logoUrl = data.get("logoUrl")
                if name:
                    party["name"] = name

                if hqAddress:
                    party["hqAddress"] = hqAddress

                if logoUrl:
                    party["logoUrl"] = logoUrl

                return party

    # Delete specific party

    def delete_party(self, id):
        for party in self.db:
            if party["id"] == id:
                self.db.remove(party)

# OfficeModel


class OfficeModels():

    def __init__(self):
        """Initialization."""

        self.db = offices
    # Create office

    def create(self, type, name):

        office = {
            "id": len(self.db)+1,
            "type": type,
            "name": name,
        }
        self.db.append(office)
        return office
    

    
parties = []

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
parties = []

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

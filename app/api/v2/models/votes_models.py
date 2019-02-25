from app.database_config import init_db
from .basemodels import BaseModel


class VotesModel(BaseModel):
    def __init__(self, candidate="candidate", voter="voter", office="office"):
        self.candidate = candidate
        self.voter = voter
        self.office = office

    def save(self):
        vote = {
            "candidate": self.candidate,
            "voter": self.voter,
            "office": self.office
        }

        connect = init_db()
        cur = connect.cursor()
        if BaseModel().check_if_item_exists('votes', 'voter', self.voter) == True:
            return "vote already exists"

        query = """ INSERT INTO votes(candidate, voter, office)VALUES\
                ( %(candidate)s, %(voter)s), %(office)s)RETURNING voter """

        cur.execute(query, vote)
        voter = cur.fetchone()[0]
        connect.commit()
        connect.close()
        return voter




    def get_votes(self):
        connect = init_db()
        cur = connect.cursor()
        query = "SELECT candidate, vote_id, voted_on, voter, office FROM votes;"
        cur.execute(query)
        data = cur.fetchall()
        res = []

        for i, items in enumerate(data):
            candidate, vote_id, voted_on, voter, office = items
        votes = dict(
            vote_id=int(vote_id),
            candidate=candidate,
            office=office,
            voter=int(voter),
            voted_on=int(voted_on)
        )
        res.append(votes)
        return res


    def get_single_vote(self, vote_id):
        connect = init_db()
        cur = connect.cursor()
        if BaseModel().check_if_item_exists('votes', 'vote_id', vote_id) == False:
            return 404

        query = "SELECT candidate, voter, voted_on FROM votes WHERE vote_id={};".format(
            vote_id)
        cur.execute(query)
        data = cur.fetchall()[0]
        res = []

        votes = dict(
            candidate=data[0],
            voter=data[1],
            voted_on=str(data[2])
        )
        res.append(votes)
        return res

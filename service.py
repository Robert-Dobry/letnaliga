from models import Team, Hrac

class Service():

    def __init__(self):
        self.players = []
        self.teams = []
        self.players_dict = []


    def create_player(self,data):
        novy_hrac = Hrac()
        novy_hrac.id = data["id"]
        novy_hrac.meno = data["meno"]
        novy_hrac.priezvisko = data["priezvisko"]
        novy_hrac.team = data["team"]
        novy_hrac.stats = data["stats"]
        self.players.append(novy_hrac)
        self.players_dict.append(novy_hrac.__dict__())
        return novy_hrac


    def get_all_players(self):
        return self.players_dict


    def get_player_by_id(self,param_id):
        for hrac in self.players:
            if hrac.id == int(param_id):
                print(hrac)
                return hrac
        return None




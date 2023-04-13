from models import Team, Hrac


players = []
players_dict = []

def create_player(data):
    novy_hrac = Hrac()
    novy_hrac.id = data["id"]
    novy_hrac.meno = data["meno"]
    novy_hrac.priezvisko = data["priezvisko"]
    novy_hrac.team = data["team"]
    novy_hrac.stats = data["stats"]
    players.append(novy_hrac)
    players_dict.append(novy_hrac.__dict__())
    return novy_hrac


def get_all_players():
    return players_dict


def get_player_by_id(id):
    print(id)
    for hrac in players:
        if hrac.id == id:
            return hrac
    return None




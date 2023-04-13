class Team():
    def __init__(self):
        id = None
        nazov = None
        hraci = []
        stats = {
            "body" : 0,
            "goly_s" : 0,
            "goly_d" : 0,
            "pocet_zapasov" : 0
        }

class Hrac():
    def __init__(self):
        id = None
        meno = None
        priezvisko = None
        team = None
        stats = {
            "goly" : 0,
            "asist" : 0,
            "tm" : 0
        }

    def __dict__(self):
        d = {
            "id" : self.id,
            "meno" : self.meno,
            "priezvisko": self.priezvisko,
            "team" : self.team,
            "goly" : self.stats["goly"],
            "asistencie" : self.stats["asist"],
            "tm" : self.stats["tm"]
        }
        return d


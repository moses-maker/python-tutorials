class Football:
    def __init__(self, country, division, no_of_times):
        self.country = country
        self.division = division
        self.no_of_times = no_of_times

    def fifa(self):
        print(f"{self.country} national football in {self.division} division")

class WorldChampions(Football):
    def world_championship(self):
        print(f"{self.country} national team is {self.no_of_times} times champs")

germany = WorldChampions("Germnay", "UEFA", "4")
germany.fifa()
germany.world_championship()

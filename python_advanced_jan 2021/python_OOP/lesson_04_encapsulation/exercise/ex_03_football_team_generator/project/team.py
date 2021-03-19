class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def get_player_by_name(self, player_name):
        try:
            player = [player for player in self.__players if player_name == player.name][0]
            return player
        except:
            return None

    def remove_player(self, player_name):
        player = self.get_player_by_name(player_name)
        if player != None:
            return player
        return f"Player {player_name} not found"

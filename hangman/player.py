class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def increase_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0
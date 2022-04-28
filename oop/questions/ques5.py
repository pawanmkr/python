class Players:
    def __init__(self):
        print("Automatically Called")

    def score(self, player_score):
        print(player_score)


p = Players()
another_object = Players()

p.score(33)


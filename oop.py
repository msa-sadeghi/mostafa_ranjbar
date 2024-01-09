class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self):
        print(f"{self.name} is moving")



player1 = Player("petty", 10)
player1.move()

player2 = Player("jack", 30)
player2.move()
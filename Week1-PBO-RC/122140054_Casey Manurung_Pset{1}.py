#122140054_Casey Z.D Manurung
import random

class Robot:
    def __init__(self, name, dps, hp):
        self.name = name
        self.dps = dps
        self.hp = hp
        self.defend = False
        self.move = 0

    def attack(self):
        return self.dps

    def regen(self):
        return self.hp

    def __str__(self):
        return f"{self.name}, Damage:{self.dps}, Current HP:{self.hp}"

class Game:
    def __init__(self):
        self.round = 0

    def beginRound(self):
        self.round += 1
        print(f"\nRound {self.round}")

    def Done(self, p1, p2):
        if p1.hp <= 0 and p2.hp > 0:
            print(f"\n{p2.name} wins!")
        elif p1.hp > 0 and p2.hp <= 0:
            print(f"\n{p1.name} wins!")
        elif p1.hp <= 0 and p2.hp <= 0:
            print("\nIt's a tie!")

        print(p1)
        print(p2)

    def attackAccuracy(self):
        return round(random.random(), 2)

    def regenEffectiveness(self):
        return round(random.uniform(0, 0.5), 2)

play = Game()

print("Player 1")
name = input("Name: ")
dps = int(input("Damage: "))
hp = int(input("Health Point: "))
p1 = Robot(name, dps, hp)

print("Player 2")
name = input("Name: ")
dps = int(input("Damage: "))
hp = int(input("Health Point: "))
p2 = Robot(name, dps, hp)

player = [p1, p2]

gameOn = True
while gameOn:
    print("\n_________________________________________________")
    play.beginRound()

    print(p1)
    print(p2)
    print("1.Attack\t2.Regen\t\t3.Defend\t4. Give up")

    for p in player:
        while p.move not in (1, 2, 3, 4):
            p.move = int(input(f"{p.name}, Choose your move: "))

        if p.move == 3:
            p.defend = True
            print(f"{p.name} activated their shield!")
        elif p.move == 2:
            add_hp = p.regen() * play.regenEffectiveness()
            print(f"{p.name}'s HP + {add_hp}")
            p.hp += add_hp
        elif p.move == 4:
            p.hp = 0

        print("--------------------------------------------------")

    if p1.move == 1:
        if p2.defend:
            print(f"{p2.name} avoided the attack! Shield broken.")
            p2.defend = False
        else:
            damage = p1.attack() * play.attackAccuracy()
            print(f"{p1.name} dealt {damage} damage!")
            p2.hp -= damage

    if p2.move == 1:
        if p1.defend:
            print(f"{p1.name} avoided the attack! Shield broken.")
            p1.defend = False
        else:
            damage = p2.attack() * play.attackAccuracy()
            print(f"{p2.name} dealt {damage} damage!")
            p1.hp -= damage

    p1.move = 0
    p2.move = 0

    if p1.hp <= 0 or p2.hp <= 0:
        gameOn = False
        play.Done(p1, p2)

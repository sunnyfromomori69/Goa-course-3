class Fighter:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def heal(self, amount):
        self.health += amount
        print(f"{self.__class__.__name__} healed by {amount}, health is now {self.health}")



class Archer(Fighter):
    def __init__(self, health, damage, speed, range, reload):
        super().__init__(health, damage, speed)
        self.range = range
        self.reload = reload


class Mage(Fighter):
    def __init__(self, health, damage, speed, spell, mana):
        super().__init__(health, damage, speed)
        self.spell = spell
        self.mana = mana



ninja = Fighter(health=80, damage=25, speed=90)
samurai = Fighter(health=120, damage=40, speed=60)
viking = Fighter(health=150, damage=50, speed=50)
warrior = Fighter(health=100, damage=35, speed=70)
veteran = Fighter(health=110, damage=45, speed=65)
tribesman = Archer(health=90, damage=20, speed=75, range=60, reload=5)
necromancer = Mage(health=70, damage=55, speed=40, spell="Raise Dead", mana=120)


ninja.heal(10)
samurai.heal(20)
tribesman.heal(15)
necromancer.heal(25)

print(vars(necromancer))
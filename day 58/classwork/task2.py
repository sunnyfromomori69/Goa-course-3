class mage:
    def __init__(self, health, damage, mana):
        self.health = health
        self.damage = damage
        self.mana = mana

Pyromancer = mage(100, 50, 200)
nycromancer = mage(200, 40, 200)

print("Health: " + Pyromancer)
print("Damage: " + Pyromancer)
print("Mana: " + Pyromancer)

2#) შექმენით Fighter კლასი და გაუწერეთ მინიმუმ 3 ატრიბუტი, შემდეგ შექმნით ამ კლასის 3 ინსტანცია და დაბეჭდეთ ერთ-ერთის თვისებები. დაწერეთ ობიექტზე ორინეტირებული პროგრამირება
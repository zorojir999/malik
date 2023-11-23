class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def hero_name(self):
        print(self.name)

    def multiply(self):
        print(self.health_points * 2)

    def crit(self):
        print(self.damage ** 2)

    def __str__(self):
        return f"Nickname: {self.nickname}; Superpower: {self.superpower}, Health points: {self.health_points}, Catchphrase: {self.catchphrase}"

    def __len__(self):
        return len(self.catchphrase)


class Air(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=None, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def multiply(self):
        print(self.health_points ** 2)
        self.fly = True

    def phrase(self):
        print("True in the True_phrase")


class Space(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=None, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def quadratic(self):
        print(self.health_points ** 2)
        self.fly = True

    def phrase(self):
        print("True in the True_phrase")


class Villain(SuperHero):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=None, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = True

    def gen_x(self):
        pass

    def crit(self):
        print(self.damage ** 2)

    def quadratic(self):
        print(self.health_points ** 2)
        self.fly = True

    def phrase(self):
        print("True in the True_phrase")


Hero = SuperHero('Batman', 'Bat', 'Batmobile', 100, 'nigga')
Hero1 = Air('Superman', 'MAN', 'fly', 110, 'wassup nigga', 233)
Hero2 = Space('Dart wader', 'max', 'sword', 122, 'i am black', 322)
Villain = Villain('Barbie', 'barb', 'stupidity', 1000000, 'you all niggas', 321)
Hero.hero_name()
Hero.multiply()
print(Hero)
print(len(Hero))
Hero1.hero_name()
Hero1.multiply()
Hero1.phrase()
Hero1.crit()
print(Hero1)
print(len(Hero1))
Hero2.hero_name()
Hero2.multiply()
Hero2.phrase()
Hero2.crit()
print(Hero2)
print(len(Hero2))

Villain.hero_name()
Villain.multiply()
Villain.phrase()
Villain.crit()
print(Villain)
print(len(Villain))


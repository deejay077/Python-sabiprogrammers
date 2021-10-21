class sharks:         # class of sharks
    def swim(self):
        print('All sharks can swim')
    def eat(self):
        print('sharks eat')
dolphin = sharks()       # instance of class sharks or object in class sharks
dolphin.swim()
dolphin.eat()

class shark:
    def __init__(self, name, age, colour):     # constructor for object variables
        self.name = name
        self.age = age
        self.colour = colour
    def swim(self):
        print('All sharks can swim')
    def eat(self):
        print('sharks eat')
    def intro(self):
        print('this is a', self.name, 'it is', self.age,'years and', self.colour )

whale = shark('blue whale', 13, 'pink')
whale.intro()

class shark:
    animal = 'fish'
    location = 'sea'
    follow = 5

    def __init__(self, name, age, colour):     # constructor for object variables
        self.name = name
        self.age = age
        self.colour = colour
    def swim(self):
        print('All sharks can swim')
    def eat(self):
        print('sharks eat')
    def intro(self):
        print('this is a', self.name, self.animal, 'it is', self.age,'years and', self.colour )


class swordfish(shark):
    def live(self):
        print('this fish lives in', self.location)

sword = swordfish('fishes',2,'brown')
sword.intro()
sword.live()

class jelly(shark):
    def __init__(self, name, age, colour, bone='boned', cartilage=True):
        self.name = name
        self.age = age
        self.colour = colour
        self.bone = bone
        self.cartilage = cartilage
jelly_fish = jelly('jelly',5,'black','boneless', False)
jelly_fish.intro()


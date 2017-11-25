
class caracter(object):
    def __init__(self):
        print("caracter created")
class hero(caracter):
    def __init__(self):
        caracter.__init__(self)
        print("hero created")
    def attack(self):
        print("enemy killed")
    def moveup(self):
        print("moving up ")
        print("moved up")
    def movedown(self):
        print("moving down ")
        print("moved down")


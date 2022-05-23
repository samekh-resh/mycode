#!/usr/bin/python3



class Wizard:
    def __init__(self):
        self.might = 5
        self.magic = 5
        self.speed = 4
        self.hp=10

    def potion(self):
        self.hp += 10

    def fireball(self, otherWizard):
        otherWizard.hp -= 6

necromancer_dao = Wizard()
wizzy_marshall = Wizard()
print(necromancer_dao.hp)
necromancer_dao.potion()
wizzy_marshall.fireball(necromancer_dao)
print(necromancer_dao.hp)

print(necromancer_dao.hp)

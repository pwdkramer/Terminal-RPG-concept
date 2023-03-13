class Character:
    def __init__(self, hit_points, armor_class, strength, constitution, dexterity, intelligence, widsom, charisma):
        self.hit_points = hit_points
        self.armor_class = armor_class
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.widsom = widsom
        self.charisma = charisma

    #getters and setters
    def get_hit_points(self):
        return self.hit_points
    def set_hit_points(self, newHP):
        self.hit_points = newHP

    def get_armor_class(self):
        return self.armor_class
    def set_armor_class(self, newAC):
        self.armor_class = newAC

    def get_strength(self):
        return self.strength
    def set_strength(self, newStr):
        self.strength = newStr
    
    def get_constitution(self):
        return self.constitution
    def set_constitution(self, newCon):
        self.constitution = newCon

    def get_dexterity(self):
        return self.dexterity
    def set_dexterity(self, newDex):
        self.dexterity = newDex

    def get_intelligence(self):
        return self.intelligence
    def set_intelligence(self, newInt):
        self.intelligence = newInt

    def get_wisdom(self):
        return self.widsom
    def set_wisdom(self, newWis):
        self.widsom = newWis

    def get_charisma(self):
        return self.charisma
    def set_charisma(self, newCha):
        self.charisma = newCha

class Warrior(Character):
    def __init__(self, hit_points, armor_class, strength, constitution, dexterity, intelligence, widsom, charisma, level, surgeCount):
        self.level = 1
        self.surgeCount = 0

class Rogue(Character):
    def __init__(self, hit_points, armor_class, strength, constitution, dexterity, intelligence, widsom, charisma, level, hidden):
        self.level = 1
        self.hidden = False

class Wizard(Character):
    def __init__(self, hit_points, armor_class, strength, constitution, dexterity, intelligence, widsom, charisma, level, spellslots):
        self.level = 1
        self.spellslots = 2
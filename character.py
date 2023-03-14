class Character:
    def __init__(self, hit_points, armor_class, strength, constitution, dexterity, intelligence, wisdom, charisma):
        self.hit_points = hit_points
        self.current_hp = hit_points
        self.armor_class = armor_class
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    #getters and setters
    def get_hit_points(self):
        return self.hit_points
    def set_hit_points(self, newHP):
        self.hit_points = newHP

    def get_current_hp(self):
        return self.current_hp
    def set_current_hp(self, newHP):
        self.current_hp = newHP
        if self.current_hp < 0:
            self.current_hp = 0

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
        return self.wisdom
    def set_wisdom(self, newWis):
        self.wisdom = newWis

    def get_charisma(self):
        return self.charisma
    def set_charisma(self, newCha):
        self.charisma = newCha

class Warrior(Character):
    def __init__(self, hit_points, armor_class, strength, constitution, dexterity, intelligence, wisdom, charisma, level, surgeCount):
        super().__init__(hit_points, armor_class, strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.level = level
        self.surgeCount = surgeCount

    def get_level(self):
        return self.level
    def level_up(self):
        self.level += 1

    def get_surgeCount(self):
        return self.surgeCount
    def set_surgeCount(self, surgeCount):
        self.surgeCount = surgeCount

class Rogue(Character):
    def __init__(self, hit_points, armor_class, strength, constitution, dexterity, intelligence, wisdom, charisma, level, hidden):
        super().__init__(hit_points, armor_class, strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.level = level
        self.hidden = hidden

    def get_level(self):
        return self.level
    def level_up(self):
        self.level += 1

    def get_hidden(self):
        return self.hidden
    def set_hidden(self, hidden):
        self.hidden = hidden

class Wizard(Character):
    def __init__(self, hit_points, armor_class, strength, constitution, dexterity, intelligence, wisdom, charisma, level, spellslots):
        super().__init__(hit_points, armor_class, strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.level = level
        self.spellslots = spellslots

    def get_level(self):
        return self.level
    def level_up(self):
        self.level += 1

    def get_spellslots(self):
        return self.spellslots
    def set_spellslots(self, spellslots):
        self.spellslots = spellslots

class Monster(Character):
    def __init__(self, hit_points, armor_class, strength, constitution, dexterity, intelligence, wisdom, charisma, name):
        super().__init__(hit_points, armor_class, strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.name = name

    def get_name(self):
        return self.name
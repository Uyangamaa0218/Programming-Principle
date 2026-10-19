super_hero_name_1 = "Peter Parker"
super_hero_name_2 = "Tony Stark"
super_hero_name_3 = "Bruce Banner"

super_hero_alias_1 = "Spiderman"
super_hero-alias_2 = "Iron Man"
super_hero_alias_3 = "The Hulk"

class SuperHero:
    def __init__(self, name="", alias="", special_skill=""):
        self.name = name
        self.alias = alias
        self.special_skill = special_skill

    def __str__(self):
        return f"{self.name}: {self.alias} - {self.special_skill}"

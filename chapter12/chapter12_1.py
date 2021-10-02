class PokemonKinds:
    def __init__ (self, name, type, attck):
        self.name = name
        #self.type1 = name
        self.type = type
        self.attck = attck

monster = PokemonKinds("チャーレム", "エスパー", 100)
print(monster.name)
print(monster.type)
print(monster.attck)

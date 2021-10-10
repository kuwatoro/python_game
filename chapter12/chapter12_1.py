class PokemonKinds:
    def __init__(self, name, type1, type2, attck):
        self.name = name
        self.type = type1
        #self.type = type2
        self.types = type2
        self.attck = attck
      
    def info(self):
        print(self.types)
        print(self.attck)
        print(self.name)
        print(self.type)

monster1 = PokemonKinds("チャーレム", "エスパー", "かくとう", 100)
monster1.info()
print(monster1.name)
print(monster1.type)

monster2 = PokemonKinds("ヌマクロー", "じめん", "みず", 40)
monster2.info()




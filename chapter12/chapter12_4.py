class Lucario:
    def __init__(self, name, attack):
        self.pokename = name
        self.pokeattack = attack

    def info(self):
        print(self.pokename)
        print(self.pokeattack)


class MegaLucario(Lucario):
    def __init__(self, name, attack, skill):
        super().__init__(name, attack)
        self.pokeskill = skill

    def info(self):
        print("ルカリオが" + self.pokename + "にメガしんかした！")
        print("こうげきりょくが{}".format(self.pokeattack) + "にあがった！")

    def wepon(self):
        print(self.pokename + "は" + self.pokeskill + "をおぼえた！")


rukario = Lucario("ルカリオ", 110)
rukario.info()

mega = MegaLucario("メガルカリオ", 145, "きあいだま")
mega.info()
mega.wepon()
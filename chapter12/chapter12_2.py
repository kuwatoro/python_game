import tkinter
FONT = ("STIXIntegralsD", 30)

class PokemonKinds:
    def __init__(self, name, type1, type2, attck, photofile):
        self.pokemonname = name
        self.pokemontype1 = type1
        self.pokemontype2 = type2
        self.pokemonattck = attck
        self.pokemonimg = tkinter.PhotoImage(file=photofile)

    def create(self, x, y):
        canvas.create_image(x+150, y+120, image=self.pokemonimg)
        canvas.create_text(x+340, y+40, text=self.pokemonname, font=FONT, fill="red")
        canvas.create_text(x+340, y+80, text=self.pokemontype1, font=FONT, fill="blue")          
        canvas.create_text(x+340, y+120, text=self.pokemontype2, font=FONT, fill="blue")
        canvas.create_text(x+340, y+160, text=self.pokemonattck, font=FONT, fill="green")

window = tkinter.Tk()
window.title("メガ進化が欲しい")
canvas = tkinter.Canvas(window, width=600, height=560, bg="white")
canvas.pack()

monster = [
    PokemonKinds("フライゴン", "ドラゴン", "じめん", 100, "image/furaigon.png"),
    PokemonKinds("チャーレム", "エスパー", "かくとう", 200, "image/charemu.png")
]
monster[0].create(0, 0)
monster[1].create(0, 240)

window.mainloop()


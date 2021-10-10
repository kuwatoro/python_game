import tkinter
import time
FONT = ("Yuanti SC", 24)

class PokemonKinds:  # ポケモンクラス
    def __init__(self, name, life, px, py, photofile, tagname):
        self.namepoke = name
        self.lifepoke = life
        self.maxpoke = life
        self.pxpoke = px
        self.pypoke = py
        self.photopoke = tkinter.PhotoImage(file=photofile)
        self.tagpoke = tagname

    def create(self):  # ポケモンの描画
        x = self.pxpoke
        y = self.pypoke
        canvas.create_image(x, y, image=self.photopoke, 
        tag=self.tagpoke)
        canvas.create_text(x, y+120, text=self.namepoke, 
        font=FONT, fill="orange", tag=self.tagpoke)
        canvas.create_text(x, y+200, text="HP{}/{}".format
        (self.lifepoke, self.maxpoke), font=FONT, fill="green",
        tag=self.tagpoke)

    def attack(self):  # 攻撃動作
        move = 1
        if self.pxpoke >= 400:
            move = -1
        for i in range(2):
            canvas.coords(self.tagpoke, 
            self.pxpoke+i*320*move, self.pypoke)
            canvas.update()
            time.sleep(0.3)
        canvas.coords(self.tagpoke, self.pxpoke, self.pypoke)

    def damage(self):  # ダメージ計算とポケモンの点滅
        for i in range(3):
            self.create()
            canvas.update()
            time.sleep(0.3)
            canvas.delete(self.tagpoke)
            canvas.update()
            time.sleep(0.3)
        self.life = self.life - 30
        if self.life > 0:
            self.create()
        else:
            print(self.namepoke+"はたおれた！")

def click_left():  # 左側のボタンを押した時
    monster[0].attack()
    monster[1].damage()

def click_right():  # 右側のボタンを押した時
    monster[1].attack()
    monster[0].damage()

window = tkinter.Tk()
window.title("たんぱんこぞうがしょうぶをしかけてきた！")
canvas = tkinter.Canvas(window, width=800, heigh=600, bg="aqua")
canvas.pack()

btn_left = tkinter.Button(text="かえんほうしゃ", command=click_left)
btn_left.place(x=150, y=430)  # 左側のボタンの配置
btn_right = tkinter.Button(text="げきりん", command=click_right)
btn_right.place(x=520, y=430)  # 右側のボタンの配置

monster = [
    PokemonKinds("リザードン", 153, 200, 210, "image/riza-don.png", "RP"),
    PokemonKinds("ガブリアス", 184, 550, 210, "image/gaburiasu.png", "LP")
]
monster[0].create()
monster[1].create()

window.mainloop()
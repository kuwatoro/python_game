# 自爆スイッチの配置
import tkinter

def click_btn():
    jibaku["text"] = "押してしまった……"

window = tkinter.Tk()
window.title("自爆スイッチ")
window.geometry("1000x550")

jibaku = tkinter.Button(window, text="自爆スイッチ〜絶対に押すな！と言われたら押したくなっちゃうよね〜", 
font=("Toppan Bunkyu Mincho", 24), command=click_btn)

jibaku.place(x=60, y=200)
window.mainloop()

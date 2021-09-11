# 複数のテキスト入力欄の作成
import tkinter

# ボタンが押された時の関数
def btn():
    text.insert(tkinter.END, "オベリスクの巨神兵")  # insertm()命令で、入力欄に文字列を追加
                                                 # tkinter.ENDで"オベリスクの巨神兵"はテキストの最後尾に追加される

window = tkinter.Tk()
window.title("複数のテキスト入力")
window.geometry("800x600")

# ボタンの作成
button = tkinter.Button(text="押すなよ、押すなよ！", fg="orchid", command=btn)
button.place(x=40, y=40)
# button.pack()

# テキスト入力欄の作成
text = tkinter.Text(font=("Baloo Paaji", 22), fg="tomato", bg="skyblue")
text.place(x=100, y=300, width=600, height=300)
# text.pack()

window.mainloop()
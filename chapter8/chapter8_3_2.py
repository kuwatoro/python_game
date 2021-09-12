# キー入力でリアルタイム処理
import tkinter

key = ""            # キーの値を入れる変数の宣言
def key_down(e):    # キーを押したときに実行する関数の定義
    global key
    key = e.keysym  # 押されたキーの名称をkeyに代入

def key_click():                   # キーが押されたらリアルタイム処理を実行するための関数の定義
    label["text"] = key            # 上で代入されたkeyを今度はラベルに代入
    window.after(2000, key_click)  # after()命令で2秒後にkey_click関数が実行される

window = tkinter.Tk()
window.title("リアルタイムキー入力")
window.geometry("400x300")

# bind()命令
window.bind("<KeyPress>", key_down)  # キーが押されたらkey_down関数を実行
label = tkinter.Label(font=("Bodoni 72 Oldstylea", 80))
label.pack()
key_click()                         # キーが押されたらkey_clickも実行

window.mainloop()
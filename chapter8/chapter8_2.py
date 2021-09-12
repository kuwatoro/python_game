# キーコードの取得
import tkinter

key = 0
def key_down(event):  # キーを押すと関数が実行
    global key
    key = event.keycode       # 押されたキーのコードをkeyに代入
    print("KEY:" + str(key))  # 何かキーを押すと数値となって表示される

window = tkinter.Tk()
window.title("キーコードの取得")

window.bind("<KeyPress>", key_down)  
# bind("<イベント>", イベント発生時に実行する関数)
# <KeyPress>はキーを押したという意味。他にもいろいろある
window.mainloop()
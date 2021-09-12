# リアルタイム
import tkinter

time = 0
def count_up():
     global time                   # グローバル変数
     # time = 0  # ローカル変数にしてしまうと関数を呼び出すたびに初期値になってしまうので1のまま変化しなくなる
     time = time + 1               # 関数が実行されると+1 つまり1秒追加される
     label["text"] = time          # ⭐️ラベルにtimeの値を表示
     window.after(1000, count_up)  # 2回目からは1秒ごとにこっちの関数が実行

window = tkinter.Tk()
window.title("リアルタイム処理")
window.geometry("400x300")

# ラベルの表示
label = tkinter.Label(font=("LiSong Pro", 80))  # ⭐️timeの値が入る
label.pack()
window.after(1000, count_up)  # after(ミリ秒, 実行する関数名) 一番最初はlabelの関数が実行

window.mainloop()
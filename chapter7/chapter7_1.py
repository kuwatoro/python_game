# テキスト入力欄の作成
import tkinter

# ボタンをクリックしたときに実行する関数を定義
def click_btn():
    txt = entry.get()     # 入力欄の文字列を変数txtに代入（ get()命令でEntryの文字を取得 ）
    button["text"] = txt  # ボタンの中に文字列を表示

window = tkinter.Tk()
window.title("テキスト入力欄")
window.geometry("800x600")

# テキスト入力欄作成
entry = tkinter.Entry(width=20)  # 半角２０文字の入力欄を作る
entry.place(x=20, y=30)          # 入力欄の配置

# ボタンの作成
button = tkinter.Button(text="入力後、ボタンのクリック", command=click_btn)  # command=でクリック時に実行する関数の指定
button.place(x=20, y=60)  # ボタンの配置

window.mainloop()  
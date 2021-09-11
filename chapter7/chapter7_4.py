# メッセージボックスの作成
import tkinter
import tkinter.messagebox  # messageboxモジュールをインポート

# ボタンをクリックした時の関数を定義
def c_btn():
    tkinter.messagebox.showinfo("情報", "再起動します……")    # showinfo()命令でメッセージボックスを表示
    # tkinter.messagebox.showwarning("危険！", "おしまいDETH!")  # showwarningで警告表示

window = tkinter.Tk()
window.title("メッセージボックス")
window.geometry("800x600")

# ボタンの作成
btn = tkinter.Button(text="絶対に押さないでください", command=c_btn)
btn.pack()

window.mainloop()
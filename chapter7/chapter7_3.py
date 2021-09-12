# チェックボタンの作成
import tkinter

# チェックボタンをクリックしたら実行される関数の定義
def check():
    if cval.get() == True:  # もしチェックされていたら（ get()でチェックの取得 ）
        print("チェックされています。")
    else:
        print("チェックされていません。")

window = tkinter.Tk()
window.title("チェックボタンの作成")
window.geometry("800x600")

# チェックボタンの作成
  # チェックの有無を知る
cval = tkinter.BooleanVar()  # ⭐️BooleanVarオブジェクトを用意
cval.set(False)              # cval変数にTrueまたはFalseをセット（Trueで最初からチェックあり、Falseでチェックなし）

cbtn = tkinter.Checkbutton(text="チェックボタン", 
variable=cval, command=check)  # ⭐️variable=でオブジェクトを指定し、上のBooleanVar()と結びつく 
cbtn.place(x=20, y=20)

window.mainloop()
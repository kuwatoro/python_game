# おみくじソフトを作る
import tkinter                  # tkinterモジュールをインポート
import random                   # randomモジュールをインポート
from PIL import Image, ImageTk  # ImageTkを指定することで下でImagaTkが使える

  # おみくじを引くボタンをクリックした時の動作
def click_btn():
    label["text"] = random.choice(["大吉", "吉", "中吉", "末吉", "凶", "大凶"])
    label.update()  # 文字をすぐに更新 入れないと更新するのに少し時間がかかる

  # windowを描く
window = tkinter.Tk()

  # タイトルの表示
window.title("絶対に当たってはいけないおみくじ")

  # resizabelでウィンドウサイズの固定
window.resizable(False, False)  # サイズ変更を許可する場合はTrue、許可しない場合はFalse

  # キャンバスを作る（サイズとかの指定）
canvas = tkinter.Canvas(window, width=1100, height=600, bg="pink")
canvas.pack()  # キャンバスを中央上部に配置

  # 画像の準備
omikuji = Image.open("image/simada.png")  # 画像を読み込み
omikuji = ImageTk.PhotoImage(omikuji)

  # キャンバスに画像を配置
canvas.create_image(400, 300, image=omikuji)  # キャンバスから見て画像がどの位置にくるか決まる

  # ラベルを作る
label = tkinter.Label(window, text="？？？？？？", 
font=("Baloo Paaji", 40), fg="khaki", bg="black")  # ラベルのフォント、サイズ、背景色の指定
label.place(x=540, y=140)                 # windowから見てどこに配置されるか

  # ボタンを作る
button = tkinter.Button(window, text="ゲッターズ飯田より信用あるおみくじを引く", 
font=("STIXIntegralsUpSm", 26), command=click_btn, fg="magenta")  # click_btnはクリックした時の動作の関数
button.place(x=380, y=480)                   # windowから見てどこに配置されるか

  # 最後にウィンドウを表示
window.mainloop()


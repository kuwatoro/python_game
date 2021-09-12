import tkinter
from PIL import Image, ImageTk  # ImageTkを指定することで下でImagaTkが使える

# キーを押す、離した時の処理
key = ""            # キーの値を入れるため空の箱を用意
def key_down(e):    # キーを押した時の関数の定義
    global key
    key = e.keysym  # 押したキーの名称key変数に代入（例えば↑キーなら"Up"が入る）
def key_up(e):      # キーを離した時の関数の定義
    global key
    key = ""        # キーを離したらkey変数に空の文字を代入

  # 以下は十字キーが押された時のみキャラクターが反応する
  # それ以外のキーが押されてもkey変数に空の文字が代入されているので結果何も起こらない
cx = 400            # キャラクターのx座標を管理する変数
cy = 300            # キャラクターのy座標を管理する変数
def main_proc():
    global cx,cy
    if key == "Up":    # ↑キーの名称は"Up"
        cy = cy - 20   # よってy軸の上方向に動く
    if key == "Down":  
        cy = cy + 20
    if key == "Left":
        cx = cx - 20
    if key == "Right":
        cx = cx + 20
    canvas.coords("charemu", cx, cy)  # coords()命令は表示中の画像を新しい位置に移動する
    # coords(タグ名、x座標、y座標)
    window.after(10, main_proc)       # after()命令でmain_procは0.01秒後に実行

window = tkinter.Tk()
window.title("リアルタイムにキャラクターを動かす")

# bind()命令
window.bind("<KeyPress>", key_down)  # キーを押した時に実行する関数の指定
window.bind("<KeyRelease>", key_up)  # キーを離した時に実行する関数の指定

# キャンバスの表示
canvas = tkinter.Canvas(width=800, heigh=600, bg="palegreen")
canvas.pack()

# 画像の配置
photo = Image.open("charemu.png")                        # 画像を開く
photo = ImageTk.PhotoImage(photo)                        # 画像の読み込み
canvas.create_image(cx, cy, image=photo, tag="charemu")  # キャンバスに画像の表示 tag=はその画像の名前みたいなもの？

main_proc()  # main_proc()関数の実行（キーを押すか離した時に実行される）

window.mainloop()
# 二次元リストで迷路ゲーム
import tkinter
from PIL import Image, ImageTk  # ImageTkを指定することで下でImagaTkが使える
# import tkinter.messagebox       # messageboxモジュールをインポート

# キーを押した、離した時の関数の定義
key = ""
def key_down(e):
    global key
    key = e.keysym  # 押したキーの名称をkey変数に代入
def key_up(e):
    global key
    key = ""        # キーを離したら空の文字を代入

# キーを押した、離した時に実行するリアルタイム処理を行う関数の定義
cx = 1    # 最初に設定しておくことでmeiro[1][1]のマスからスタートできる
cy = 1
nuri = 0  # 色を塗ったマスを数えるための変数
def game_start():
    global cx, cy, nuri
    # 間違えた時のやり直し処理
    if key == "Shift_L" and nuri > 1:  # もしシフトを押したかつ、2マス以上塗っていた時
        canvas.delete("nurinuri")      # 塗ったマスを削除。ここまでの記述だと塗ったマスを全て削除するだけになる
        cx = 1                         # キャラクターの位置を初期値に戻す
        cy = 1
        nuri = 0                       # 塗ったマスのカウントも初期値に戻す
        for y in range(7):
            for x in range(10):
                if meiro[y][x] == 2:   # もし塗ったマスがあれば
                    meiro[y][x] == 0   # 値を0にする（塗っていない状態に戻す）

    # 方向キーが押された時の処理
    if key == "Up" and meiro[cy-1][cx] == 0:  # 方向キーが上に押されるかつ、現在位置の上のマスが0（通路）なら
        cy = cy - 1                           # y軸の現在位置を1減らす（画像が1マス上に進む）
    if key == "Down" and meiro[cy+1][cx] == 0:
        cy = cy + 1
    if key == "Left" and meiro[cy][cx-1] == 0:
        cx = cx - 1
    if key == "Right" and meiro[cy][cx+1] == 0:
        cx = cx + 1
    
    # キャラクターのいる位置に色を塗る処理
    if meiro[cy][cx] == 0:  # もしキャラクターのいる場所が0（通路）なら
        meiro[cy][cx] == 2  # meiroリストの値を2にする
        nuri = nuri + 1     # 何マス塗ったかカウント

        # キャラクターがいる場所に色のついた矩形を作る（キャラクターのいるマスに色を塗る）
        canvas.create_rectangle(cx*80, cy*80, (cx*80)+79, (cy*80)+79, fill="purple", width=1, tag="nurinuri")

    # キャラクターを一度削除
    canvas.delete("mimi")  
    # 削除したキャラクターをもう一度表示する
    canvas.create_image((cx*80)+40, (cy*80)+40, image=photo, tag="mimi")  
    
## <!-- messageboxやろうとしたけどcanvas.update()がうまくいかなかったので割愛 --> ##
    # if nuri == 28:  # nuri変数が28マス分溜まるとメッセージが表示される
        # canvas.update()
        # tkinter.messagebox.showinfo("おめでとう", "おめでとう！全てのマスが塗れました！")
    # canvas.coords("mimi", (cx*80)+40, (cy*80)+40)  # 方向キーが押されたらmimi画像を新しい位置に動かす
    # coords()命令だとキャラクターが色を塗った矩形に上書きされて見えなくなる
    # else:  # 28マス溜まらなければ関数は実行し続ける
    window.after(100, game_start)  # 方向キーが押された0.1秒後に関数を実行


# ウィンドウの表示
window = tkinter.Tk()
window.title("脱出できたら100万円ゲーム")

# bind()命令でキーを押した時、離した時実行する関数の指定
window.bind("<KeyPress>", key_down)
window.bind("<KeyRelease>", key_up)

# <!-- ここからキャンバスの配置 -->
canvas = tkinter.Canvas(width=800, height=560, bg="springgreen")
canvas.pack()

meiro = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,0,1,1,0,1],
    [1,0,1,1,1,1,0,0,0,1],
    [1,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

for y in range(7):
    for x in range(10):       # 横方向に10回の繰り返しを7回行う。
        if meiro[y][x] == 1:  # meiro配列が1（壁）なら、深緑の四角を作る
            canvas.create_rectangle(x*80, y*80, (x*80)+79, (y*80)+79, fill="seagreen", outline="teal")
# <!-- ここまでキャンバスの配置-- >

# 画像の配置（画像はキャンバス上で移動させるからこっちに記述したほうがいいかも）
photo = Image.open("mimi_s.png")                        # 画像を開く
photo = ImageTk.PhotoImage(photo)                        # 画像の読み込み
canvas.create_image((cx*80)+40, (cy*80)+40, image=photo, tag="mimi")  # キャンバスに画像の表示 tag=はその画像の名前みたいなもの？
  # +40にしているのは指定している座標が画像の中心になるため

game_start()

window.mainloop()
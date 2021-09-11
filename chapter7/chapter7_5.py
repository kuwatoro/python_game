# 診断ゲーム
import tkinter
from PIL import Image, ImageTk  # ImageTkを指定することで下でImagaTkが使える

# 診断結果の配列
kekka = [
"よかったね、人間です",
"まだ大丈夫、人間です。",
"あれ？ネコ……？",
"ネコだろ、キミ。",
"キャットフード食べる？",
"猫の手も借りたい",
"もう諦めろ、きみは1000％ネコだ",
"サイコパスです"
]

# 診断するボタンがクリックされた時の関数を定義
def c_btn():
    pts = 0                        # チェックしたボタンを数える変数
    for i in range(7):             # チェックボタンの数だけ繰り返し
        if bvar[i].get() == True:  # その質問がチェックされていたら
            pts = pts + 1          # pts変数に1を足す（カウントする）
    neko = int(100*pts/7)          # "ネコ度"を計算、int関数で数値に

    text.delete("1.0", tkinter.END)                # テキスト入力欄の文字を削除（入力欄に文字がない状態にしたいため）
    text.insert("1.0", "<診断結果>/nあなたのネコ度は" + str(neko) + "％です。/n" + kekka[pts])
    # 最後に診断結果を表示。str関数でネコ度は数値に。結果はkekka配列から拾ってくる。
    # "1.0"は入れないと入力欄に出力されない

window = tkinter.Tk()
window.title("診断アプリ")
window.resizable(False, False)

# キャンバスの作成
canvas = tkinter.Canvas(window, width=900, height=700)
canvas.pack()

# 画像の配置
photo = Image.open("sumire.png")            # 画像を開く
photo = ImageTk.PhotoImage(photo)           # 画像の読み込み
canvas.create_image(400, 300, image=photo)  # 画像の表示

# ボタンの作成
button = tkinter.Button(text="診断する", font=("PilGi", 48), bg="plum", command=c_btn)
button.place(x=400, y=480, width=200, height=80)

# テキスト入力欄の作成
text = tkinter.Text(font=("Khmer MN", 16), fg="pink")
text.place(x=320, y=30, width=420, height=120)

# 複数のチェックボタンの配置
  # 項目が7つあるので何も入っていない箱を7つ用意する
bvar = [None]*7  # BooleanVarのオブジェクト用のリスト
cbtn = [None]*7  # チェックボタン用のリスト
  # チェックボタンの質問
item = [
"高いところから人間を見下すのが好き",
"ボールを見ると物を壊したくなる",
"びっくりすると毛を逆立ててめっちゃキレる",
"ネズミの玩具を見ると本性を表す",
"血の匂いに敏感",
"魚の骨もかじりつきたいほど日々飢えている",
"夜、興奮する"
]

for i in range(7):  # 繰り返しで7つチェックボタンの配置
    bvar[i] = tkinter.BooleanVar()  # ⭐️BooleanVarオブジェクトを用意
    bvar[i].set(False)              # 設定したオブジェクトにFalseをセットして最初からチェックが入らないように
    cbtn[i] = tkinter.Checkbutton(text=item[i], font=("Tiro Tamil", 12),variable=bvar[i], bg="#dfe")
    # チェックボタンとセットで質問事項も表示させる
    # text=、font=で質問の表示と設定
    # ⭐️variable=でオブジェクトを指定し、上のBooleanVar()と結びつく 
    cbtn[i].place(x=400, y=160+40*i)  # チェックボタンを配置

window.mainloop()
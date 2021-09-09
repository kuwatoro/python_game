# 逃げた犯人を探す
import random
import datetime
RECORO = [
"a", "b", "c", "d", "e", "f", "g",
"h", "i", "j", "k", "l", "m", "n",
"o", "p", "q", "r", "s", "t", "u",
"v", "w", "x", "y", "z"
]

r = random.choice(RECORO)  # RECORO配列の一文字をランダムに決める
toyota = " "

for i in RECORO:
    if i != r:  # ランダムに決めた文字と一致しなければ変数toyotaに追加
        toyota = toyota + i
print(toyota)  # ランダムに決めた文字以外出力
start_time = datetime.datetime.now()  # 開始時間を入れる

plyear = input("逃げた犯人は？")
print("犯人は" + plyear + "だな？！")  
if plyear == r:
    print("正解です")
    end_time = datetime.datetime.now()  # 終了時間を入れる
    print(str((end_time - start_time).seconds) + "秒かかりました。")  # 終了から開始時間を引いて何秒かかったか出力
else:
    print("違います")



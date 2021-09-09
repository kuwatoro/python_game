# 海馬社長とスゴロクバトル
import random
p_a = 1
p_b = 1
def masu():
    print("・" * (p_a-1) + "K" + "・" * (30-p_a) + "Goal")
    print("・" * (p_b-1) + "Y" + "・" * (30-p_b) + "Goal")
masu()
print("海馬：スゴロク開始の宣言をしろ、磯野！")
print("磯野：スゴロク開始イィ！")

while True:  # 無限ループ
    input("海馬：俺のターンだ！")
    p_a = p_a + random.randint(1, 6)
    if p_a > 30:  # 30マス超えると
        p_a = 30  # p_aを強制的に30にする
    masu()
    if p_a == 30:  # 30マスに達すると
        print("俺の勝ちだ！ウハハハハ！！")
        break

    input("海馬：貴様のターンだ！")
    p_b = p_b + random.randint(1, 6)
    if p_b > 30:
        p_b = 30
    masu()
    if p_b == 30:
        print("海馬：なかなかの強かさだ。褒めてやろう。")
        break
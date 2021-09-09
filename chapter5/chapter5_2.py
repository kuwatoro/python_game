# 海馬社長クイズ
Q = [
"Q1:海馬コーポレーションの社長は？",
"O2:Q1のキャラクターの切り札といえば？",
"Q3:滅びの〇〇〇〇〇〇〇!"]

A = ["海馬瀬人", "青眼の白龍", "バーストストリーム"]
A2 = ["かいばせと", "ブルーアイズホワイトドラゴン", "バーストストリーム"]

for i in range(3):
    print(Q[i])
    anser = input()
    #print(anser)

    if anser == A[i] or anser == A2[i]:
        print("正解！全速前進DA！")
    else:
        print("不正解！貴様、それでも決闘者か！")
        break
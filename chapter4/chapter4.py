import random
cnt = 0
while True:
    card = random.randint(1, 1000)
    print(card)
    cnt = cnt + 1
    if card == 999:
        break
print(str(cnt) + "回目でブラックマジシャンをゲット⭐️")
print(card)

# 迷路の自動生成
import pygame
import sys
import random

from pygame.constants import WINDOWEXPOSED

Beige          = (245,245,220)
DarkTurquoise	 = (  0,206,209)

MEIRO_X = 11  # 横に何マスあるか
MEIRO_Y = 9   # 縦に何マスあるか
meiro = []    # 迷路のデータを入れるリスト

for y in range(MEIRO_Y):            # 縦マス分繰り返し
    meiro.append([0] * MEIRO_X)  # append()命令と繰り返しで二次元リストを簡潔にまとめる

# ⭐️ 迷路を作る関数
def make_danjon():
    XW = [0, 1, 0, -1]
    YH = [-1, 0, 1, 0]

    # ①周囲の壁を作る。0は床、1は壁や柱になる。
    for x in range(MEIRO_X):
        meiro[0][x] = 1          # 横軸一番上段の処理
        meiro[MEIRO_Y-1][x] = 1  # 横軸一番下段の処理
    for y in range(MEIRO_Y):
        meiro[y][0] = 1          # 縦軸一番左の処理
        meiro[y][MEIRO_X-1] = 1  # 縦軸一番右の処理

    # ②中身は壁や柱を作らない
    for y in range(1, MEIRO_Y-1):      # 1〜8まで繰り返し
        for x in range(1, MEIRO_X-1):  # 1〜10まで繰り返し
            meiro[y][x] = 0            # 壁の内側には何も作らない

    # ③周囲の壁から1マスおきに柱を作る
    #for y in range(2, MEIRO_Y-2, 2):      # 2〜7まで繰り返し。2ずつ増やす（下に増えていく）
    #    for x in range(2, MEIRO_X-2, 2):  # 2〜9まで繰り返し。2ずつ増やす（右に増えていく）
    #        meiro[y][x] = 1               # 縦横軸共に1マスおきに柱を作る

    # ④柱から上下左右に壁を作る
    #for y in range(2, MEIRO_Y-2, 2):      # 2〜7まで繰り返し。2ずつ増やす（下に増えていく）
    #    for x in range(2, MEIRO_X-2, 2):  # 2〜9まで繰り返し。2ずつ増やす（右に増えていく）
    #     r = random.randint(0, 3)         # ランダムで0~3を選ぶ
    #     if x > 2:                        # 二列目から左に壁を作れないため二列目から下のrandomを使う
    #          r = random.randint(0, 2)    # ランダムで0~2を選ぶ
    #     meiro[y + YH[r]][x + XW[r]] = 1

# ⭐️ メイン処理を行う関数
def game():
    pygame.init()
    pygame.display.set_caption("迷路ゲーム(qキーで更新)")
    scene = pygame.display.set_mode((660, 540))
    clock = pygame.time.Clock()

    make_danjon()  # メイン処理を行ってから迷路を作る関数を呼び出す（一番最初の迷路が出る）
                  # ここに記述が無いと一番初めはまっさらな画面からスタート

    # 実際に迷路を出力
    while True:
        for btn in pygame.event.get():
            if btn.type == pygame.QUIT:     # 閉じるボタンを押した時
                pygame.quit()               # pygameの終了
                sys.exit()                  # ウィンドウを閉じる
            if btn.type == pygame.KEYDOWN:  # 何かキーを押すイベントが発生した時
                if btn.key == pygame.K_q:   # qキーが押されたら
                    make_danjon()            # 新しく迷路を作る関数を実行

        # 迷路のマスに色を塗ったりサイズを決める
        for y in range(MEIRO_Y):
            for x in range(MEIRO_X):
                W = 60   # 1マスの幅
                H = 60   # 1マスの高さ
                X = x*W  # x座標の計算
                Y = y*H  # y座標の計算
                if meiro[y][x] == 0: # 通路
                    pygame.draw.rect(scene, Beige, [X, Y, W, H])
                if meiro[y][x] == 1: # 壁・柱
                    pygame.draw.rect(scene, DarkTurquoise, [X, Y, W, H])

        pygame.display.update()
        clock.tick(2)

if __name__ == '__main__':
    game()

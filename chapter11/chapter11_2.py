# ダンジョンを作る
import pygame
import sys
import random

BLACK  = (  0,  0,  0)  # 黒色
ENJI   = (179, 66, 74)  # えんじ色
PERU   = (205,133, 63)  # 茶色

# 迷路を作るリスト
MEIRO_X = 11                   # 迷路の横方向は何マスか
MEIRO_Y = 9                    # 迷路の縦方向は何マスか
meiro = []                     # 迷路のデータを入れるリスト
for y in range(MEIRO_Y):       # 繰り返しとappend()命令で二次元リストを簡潔にまとめる
    meiro.append([0]*MEIRO_X)  # 0*11個が９行の意味

# ダンジョンを作るリスト
DANJON_X = MEIRO_X*3             # ダンジョンの横方向は何マスか
DANJON_Y = MEIRO_Y*3             # ダンジョンの縦方向は何マスか
danjon = []                      # ダンジョンのデータを入れるリスト
for y in range(DANJON_Y):        # 繰り返しとappend()命令で二次元リストを簡潔にまとめる
    danjon.append([0]*DANJON_X)  # 0*33個が27行の意味

photowall = pygame.image.load("wall.png")    # ダンジョン壁の画像
photofloor = pygame.image.load("floor.png")  # ダンジョン床の画像

# ⭐️ ダンジョンの自動生成
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
    for y in range(2, MEIRO_Y-2, 2):      # 2〜7まで繰り返し。2ずつ増やす（下に増えていく）
        for x in range(2, MEIRO_X-2, 2):  # 2〜9まで繰り返し。2ずつ増やす（右に増えていく）
            meiro[y][x] = 1               # 縦横軸共に1マスおきに柱を作る
    # ④柱から上下左右に壁を作る
    for y in range(2, MEIRO_Y-2, 2):      # 2〜7まで繰り返し。2ずつ増やす（下に増えていく）
        for x in range(2, MEIRO_X-2, 2):  # 2〜9まで繰り返し。2ずつ増やす（右に増えていく）
         r = random.randint(0, 3)         # ランダムで0~3を選ぶ
         if x > 2:                        # 二列目から左に壁を作れないため二列目から下のrandomを使う
              r = random.randint(0, 2)    # ランダムで0~2を選ぶ
         meiro[y + YH[r]][x + XW[r]] = 1

    # 🌟 迷路からダンジョンを作る
    # 最初は全体を壁にする(迷路は一旦関係なし。新しく27x33のマスを作る)
    for y in range(DANJON_Y):      # 二重ループ
        for x in range(DANJON_X):  # 33回の繰り返しを27回繰り返す
            danjon[y][x] == 9      # danjonの値は全て1（壁）になる
    # 全体を壁にした後、部屋と通路を配置していく
    for y in range(1, MEIRO_Y-1):      # 二重ループ 1〜8まで繰り返し
        for x in range(1, MEIRO_X-1):  # 1〜10まで繰り返し
            d_x = (x*3) +1
            d_y = (y*3) +1
            if meiro[y][x] == 0:                # 迷路のデータを確認し、0（床）であれば
                if random.randint(0, 99) < 15:  # 15%の確率で部屋を作る。そうでなければ通路を作る
                    # 部屋を作る
                    for r_y in range(-1, 2):
                        for r_x in range(-1, 2):
                            danjon[d_y + r_y][d_x + r_x] = 0
                    # 通路を作る
                    else:  # 部屋をつくらないなら通路を作る
                        danjon[d_y][d_x] = 0
                        if meiro[y-1][x] == 0:
                            danjon[d_y-1][d_x] = 0
                        if meiro[y+1][x] == 0:
                            danjon[d_y+1][d_x] = 0
                        if meiro[y][x-1] == 0:
                            danjon[d_y][d_x-1] = 0
                        if meiro[y][x+1] == 0:
                            danjon[d_y][d_x+1] = 0

def game():
    pygame.init()
    pygame.display.set_caption("ダンジョンダンダンジョンジョン")
    scene = pygame.display.set_mode((1056, 432))
    clock = pygame.time.Clock()

    make_danjon()

    while True:
        for btn in pygame.event.get():
            if btn.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if btn.type == pygame.KEYDOWN:
                if btn.key == pygame.K_q:
                    make_danjon()

        # 迷路を表示
        for y in range(MEIRO_Y):
            for x in range(MEIRO_X):
                WX = x*48
                HY = y*48
                if meiro[y][x] == 0:
                    pygame.draw.rect(scene, ENJI, [WX, HY, 48, 48])
                if meiro[y][x] == 1:
                    pygame.draw.rect(scene, PERU, [WX, HY, 48, 48])

        # ダンジョンの描画
        for y in range(DANJON_Y):
            for x in range(DANJON_X):
                WX = (x*16) +528
                HY =  y*16
                if danjon[y][x] == 0:
                    scene.blit(photofloor, [WX, HY])
                if danjon[y][x] == 9:
                    scene.blit(photowall, [WX, HY])

        pygame.display.update()
        clock.tick(2)

if __name__ == '__main__':
    game()

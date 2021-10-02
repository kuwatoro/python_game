import pygame
import sys
import random

black = (0, 0, 0)

MEIRO_X = 11  # 迷路のリストを作るよ
MEIRO_Y = 9
meiro = []
for y in range(MEIRO_Y):
    meiro.append([0]*MEIRO_X)

DANJON_X = MEIRO_X *3  # ダンジョンのリストを作りまーす
DANJON_Y = MEIRO_Y *3
danjon = []
for y in range(DANJON_Y):
    danjon.append([0]*DANJON_X)

photoWall = pygame.image.load("sample/image/wall.png")     # 使う画像
photoFloor = pygame.image.load("sample/image/floor.png")
photoPlayer = pygame.image.load("sample/image/player.png")

kirito_x = 4  # 主人公の座標
kirito_y = 4

def create_danjon():  # ダンジョン作るでやんす  ※ 0=床、1=壁
    
    DNX = [0, 1, 0, -1]  # 柱から壁を作るための値でやんす
    DNY = [-1, 0, 1, 0]  # 44行目から使うでやんす
    # 迷路の周囲の壁から作っていくでやんす
    for x in range(MEIRO_X):  # まずは上下段から
        meiro[0][x] = 1
        meiro[MEIRO_Y-1][x] = 1
    for y in range(1, MEIRO_Y):  # 次は左右の壁じゃい！
        meiro[y][0] = 1
        meiro[y][MEIRO_X-1] = 1
    # 周囲の壁ができたら中身は床にするでやんす
    for y in range(1, MEIRO_Y-1):      # 縦列 1~8回繰り返す
        for x in range(1, MEIRO_X-1):  # 横列 1~10回繰り返す
            meiro[y][x] = 0
    # 1マスおきに柱を作っていくでやんす
    for y in range(2, MEIRO_Y-2, 2):      # 縦列 2~7回繰り返し、2ずつ増える（下側に作っていく）
        for x in range(2, MEIRO_X-2, 2):  # 横列 2~9回繰り返し、2ずつ増える（右側に作っていく）
            meiro[y][x] = 1
    # 40行目で作った柱から上下左右に壁を作っていくでやんす
    for y in range(2, MEIRO_Y-2, 2):      # 縦列 2~7回繰り返し、2ずつ増える（下側に作っていく）
        for x in range(2, MEIRO_X-2, 2):  # 横列 2~9回繰り返し、2ずつ増える（右側に作っていく）
         kabe = random.randint(0, 3)      # 柱の左1行目は左側に作ってもOKでやんす
         if x > 2:                        # 柱の左2行目からは左側に作れないでやんす
             kabe = random.randint(0, 2)
         meiro[y+DNY[kabe]][x+DNX[kabe]] = 1  # kabeにはランダムで0,1,-1が入るでやんす

    # 29行目から作った迷路を元にダンジョンを作っていくでやんす
    # まずはダンジョン全体を壁にするでやんす  ※ 9=壁
    for y in range(DANJON_Y):      # 14行目でx3してるので27回繰り返すでやんす
        for x in range(DANJON_X):  # 13行目でx3してるので33回繰り返すでやんす
            danjon[y][x] = 9
    # 部屋と通路を配置していくでやんす
    for y in range(1, MEIRO_Y-1):      # 36行目と同じ記述
        for x in range(1, MEIRO_X-1):
            dnx = x*3+1              # 14行目でx3してるのでこっちも3倍でやんす！
            dny = y*3+1              # 13行目でx3してるのでこっちも3倍でやんす！
            if meiro[y][x] == 0:       # 迷路のデータで0（床）のマスなら
                if random.randint(0, 99) < 15:  # 15%の確率で部屋を作るでやんす
                    for rny in range(-1, 2):
                        for rnx in range(-1, 2):
                            danjon[dny+rny][dnx+rnx] = 0  # 3x3マスを床にする
                else: # 通路を作る
                    danjon[dny][dnx] = 0     # ダンジョンが床かどうか調べる
                    if meiro[y-1][x] == 0:      # 迷路が床であれば
                        danjon[dny-1][dnx] = 0  # ダンジョンも床にする
                    if meiro[y+1][x] == 0:
                        danjon[dny+1][dnx] = 0
                    if meiro[y][x-1] == 0:
                        danjon[dny][dnx-1] = 0
                    if meiro[y][x+1] == 0:
                        danjon[dny][dnx+1] = 0

def paint_danjon(jojo):          # ダンジョンを描いていく
    jojo.fill(black)             # 黒色の背景を描く
    for y in range(-5, 6):       # 主人公を中心に上下左右5マスに画像を配置する
        for x in range(-5,6):
            wx = (x+5)*16        # wxには0〜160の数字が入る
            hy = (y+5)*16
            dnnx = kirito_x + x  # kiritoの値はキャラクターが移動するたびに変わる
            dnny = kirito_y + y
            if 0 <= dnnx and dnnx < DANJON_X and 0 <= dnny and dnny < DANJON_Y:
                if danjon[dnny][dnnx] == 0:
                    jojo.blit(photoFloor, [wx,hy])  # x,y軸ともに0、16、32の順で画像を配置
                if danjon[dnny][dnnx] == 9:
                    jojo.blit(photoWall, [wx,hy])
            if x == 0 and y == 0:  # 主人公の配置
                jojo.blit(photoPlayer, [wx,hy-8])
# if 0 <= dnnx and dnnx < DANJON_X and 0 <= dnny and dnny < DANJON_Y:
# x,y軸とも0より大きいとき画像を配置する。つまり一番周囲のマスには画像を配置せず、黒色の背景が映る。

def walk_kirito():  # 主人公の移動
  global kirito_x, kirito_y  # ボタンを押すごとに主人公の位置を変えたいので、グローバル変数の宣言
  btn = pygame.key.get_pressed()
  if btn[pygame.K_UP] == 1:
      if danjon[kirito_y -1][kirito_x] != 9: kirito_y = kirito_y -1
  if btn[pygame.K_DOWN] == 1:
      if danjon[kirito_y +1][kirito_x] != 9: kirito_y = kirito_y +1 
  if btn[pygame.K_LEFT] == 1:
      if danjon[kirito_y][kirito_x -1] != 9: kirito_x = kirito_x -1
  if btn[pygame.K_RIGHT] == 1:
      if danjon[kirito_y][kirito_x +1] != 9: kirito_x = kirito_y +1
  # 各方向キーを押した時、その方向が9（壁）でないならx、y座標を変化させる

def game_start():
    pygame.init()
    pygame.display.set_caption("ダンジョン内を考えるのをやめるまで走る")
    scene = pygame.display.set_mode((1056, 432))  # 全部画面を映したら意味ないので小さく表示
    clock = pygame.time.Clock()

    create_danjon()

    while True:
        for game in pygame.event.get():
            if game.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        paint_danjon(scene)
        walk_kirito()
        pygame.display.update()
        clock.tick(0.1)

if __name__ == '__main__':
    game_start()

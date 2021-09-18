# キー入力
import pygame
import sys

from pygame import sprite

white = (255, 255, 255)
black = (  0,   0,   0)
red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)

def game():
    pygame.init()
    pygame.display.set_caption("キー入力するぜ！")
    scene = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 90)  # pygameのフォント指定

    while True:
        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
      
        # ここからキー入力の処理
        btn = pygame.key.get_pressed()  # btnリストに全てのキーの状態を代入
        # 方向キー上下のリストの値
        updown = font.render("UP"+str(btn[pygame.K_UP]) + "DOWN"+str(btn[pygame.K_DOWN]), True, green, blue)
            # render()命令で文字列と色を指定。引数をTrueにするとフチが滑らかになる.
            # greenは文字色、blueは文字の背景色
        # 方向キー左右のリストの値
        leftright = font.render("LEFT"+str(btn[pygame.K_LEFT]) + "RIGHT"+str(btn[pygame.K_RIGHT]), True, white, red)
        # スペースキーとエンターキーのリストの値
        spcetn = font.render("SPACE"+str(btn[pygame.K_SPACE]) + "ENTER"+str(btn[pygame.K_RETURN]), white, green)

        scene.fill(black)              # 黒い画面の配置
        scene.blit(updown, [100, 100])   # blit()命令で画面にupdownを貼り付け
        scene.blit(leftright, [100, 200])
        scene.blit(spcetn, [100, 300])
        # ⭐️キーが押されていれば１、離した時は０が表示。１が表示されるのは決まりみたいなもの。

        pygame.display.update()  # 画面の更新
        clock.tick(10)           # フレームレートを指定（1秒間に約1回の処理）

if __name__ == '__main__':
    game()

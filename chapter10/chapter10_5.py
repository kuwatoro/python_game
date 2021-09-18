# マウス入力
import pygame
import sys

black  = (  0,   0,   0)
yellow = (255, 255,   0)
lime   = ( 50, 205,  50)

def game():
    pygame.init()
    pygame.display.set_caption("マウス入力しまーす")
    scene = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 90)  # pygameのフォント指定

    while True:
        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
      
        # ここからマウス入力の処理
        mosX, mosY = pygame.mouse.get_pos()  # マウスポインタの座標を変数に代入
        toyota = font.render("{},{}".format(mosX, mosY), True, yellow)  # 座標の値を画面に描く

        supra, gtr, civic = pygame.mouse.get_pressed()  # マウスボタンの状態（押しているか）を変数に代入
        honda = font.render("{}:{}:{}".format(supra, gtr, civic), True, lime)  # マウスボタンの状態を画面に描く

        scene.fill(black)               # 黒い画面を描く
        scene.blit(toyota, [100, 100])  # マウスポインタの座標を表示
        scene.blit(honda, [100, 200])   # マウスボタンの状態を表示

        pygame.display.update()  # 画面の更新
        clock.tick(10)           # フレームレートを指定（1秒間に約1回の処理）

if __name__ == '__main__':
    game()

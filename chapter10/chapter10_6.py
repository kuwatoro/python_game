# サウンド出力
import pygame
import sys

black = (  0,   0,   0)
brown = (205, 133,  63)
cyan  = (175, 238, 238)

def game():
    pygame.init()
    pygame.display.set_caption("マウス入力しまーす")
    scene = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 60)  # pygameのフォント指定
    
    try:  # 例外処理を入れてbgmとseの読み込み
        pygame.mixer.music.load("pygame_bgm.ogg")
        #bgm = pygame.mixer.Sound("pygame_bgm.ogg")
        se = pygame.mixer.Sound("pygame_se.ogg")
    except:  # 読み込みエラーの表示
        print("oggファイルが見つからないか、オーディオ機器が接続されていません")

    while True:
        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
      
        # ここからサウンド出力の処理
        btn = pygame.key.get_pressed()  # btnリストに全てのキーの状態（押したかどうか）を代入
        # bgmの再生
        if btn[pygame.K_a] == 1:                        # aキーを押したとき
            if pygame.mixer.music.get_busy() == False:  # bgmが停止中なら
                pygame.mixer.music.play(-1)             # bgmを再生
                #bgm.play()
        # bgmの停止
        if btn[pygame.K_b] == 1:                       # bキーを押したとき
            if pygame.mixer.music.get_busy() == True:  # bgmが再生中なら
                pygame.mixer.music.stop()              # bgmを停止
                #bgm.stop()
        # seの再生
        if btn[pygame.K_s] == 1:  # sキーを押したら
            se.play()             # seを再生

        # bgmの再生時間の表示
        ptime = pygame.mixer.music.get_pos()  # 再生時間を取得し、ptime変数に代入
        silvia = font.render("BGM TIME" + str(ptime), True, brown)  # 再生時間を描く
        wrx = font.render("a_play.bgm : b_stop.bgm : s_play.se", True, cyan)

        scene.fill(black)               # 黒い画面を描く
        scene.blit(silvia, [10, 150])
        scene.blit(wrx, [50, 300])
        
        pygame.display.update()  # 画面の更新
        clock.tick(10)           # フレームレートを指定（1秒間に約1回の処理）

if __name__ == '__main__':
    game()

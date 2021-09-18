# 図形を描く
import pygame  # モジュールのインポート
import sys 
import math

white  = (255, 255, 255)  # 各色の定義
black  = (  0,   0,   0)
red    = (255,   0,   0)
green  = (  0, 255,   0)
blue   = (  0,   0, 255)
gold   = (255, 216,   0)
silver = (192, 192, 192)
copper = (192, 112,  48)

# メイン処理を行う関数の定義
def game():
    pygame.init()                                # pygameの初期化
    pygame.display.set_caption("pygame 図形")     # タイトル表示
    scene = pygame.display.set_mode((800, 600))  # 画面サイズ
    clock = pygame.time.Clock()                  # 時間のオブジェクト設定
    times = 0                                    # 時間をカウントする変数

    while True:                            # 無限ループ
        times = times + 1                  # 時間を+1カウントする
        for event in pygame.event.get():   # イベントが発生したら繰り返し処理
            if event.type == pygame.QUIT:  # もし閉じるボタンが押されたら
                pygame.quit()              # pygameの終了
                sys.exit()                 # ウィンドウを閉じる

        scene.fill(black)  # 画面の色の指定

        # 線を描く
        pygame.draw.line(scene, red, [10,20], [100,200], 9)
        pygame.draw.lines(scene, blue, False, [[50,300], [150,400], [50,500]], 10)
        # 矩形を描く
        pygame.draw.rect(scene, red, [200,50, 120,80])
        pygame.draw.rect(scene, green, [200,200, 50,180], 10)
        # 多角形を描く
        pygame.draw.polygon(scene, blue, [[250,400], [200,490], [300,500]], 20)
        # 円を描く
        pygame.draw.circle(scene, gold, [400, 150], 80)
        # 楕円を描く
        pygame.draw.ellipse(scene, silver, [320,260, 80,160], 10)      # 塗りつぶしなし
        pygame.draw.ellipse(scene, copper, [400-40, 500-80, 80, 160])  # 塗りつぶしあり

        # 円弧の角度の計算
        kakudo = math.pi*times/36
        # 円弧を描く
        pygame.draw.arc(scene, blue, [600-100, 300-200, 200, 400], 0, math.pi*2)
        pygame.draw.arc(scene, white, [600-100, 300-200, 200, 400], kakudo, kakudo+math.pi/2, 5)

        pygame.display.update()  # 画面の更新
        clock.tick(10)           # フレームレートの指定

if __name__ == '__main__':
    game()
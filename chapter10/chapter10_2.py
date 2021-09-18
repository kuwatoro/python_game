# pygameでの画像表示
import pygame
import sys

# メイン処理を行う関数の定義
def game():
    pygame.init()                                # pygameの初期化（必須）
    pygame.display.set_caption("画像の表示")       # タイトル表示
    scene = pygame.display.set_mode((640, 360))  # 640x360の画面を生成
    clock = pygame.time.Clock()                  # プログラム内の時間管理に役立つオブジェクトの作成

    photo_scenery = pygame.image.load("pg_bg.png")  # 背景画像の読み込み
    photo_chara = [                                 # キャラ画像の読み込み
        pygame.image.load("pg_chara0.png"),
        pygame.image.load("pg_chara1.png")
    ]
    times = 0                                       # 時間を管理する変数timesの宣言

    # 無限ループ処理
    while True:
        times = times + 1                  # times変数の値を1増やす（時間のカウント）
        for event in pygame.event.get():   # pygameのイベント（ボタンのクリック）を繰り返しで処理する
            if event.type == pygame.QUIT:  # もし閉じるボタンが押されたら
                pygame.quit()              # pygameの終了
                sys.exit()                 # ウィンドウを閉じる

            if event.type == pygame.KEYDOWN:  # キーを押すイベントが発生した時
                # F1キーが押されたら
                if event.key == pygame.K_F1:  
                    # フルスクリーンモードにする
                    scene = pygame.display.set_mode((640, 360), pygame.FULLSCREEN)
                    # F2かEscキーが押されたら
                    if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                        # 通常状態に戻す
                        scene = pygame.display.set_mode((640, 360)) 

        x = times%160
        for i in range(5):                           # 画面に背景画像描画
            scene.blit(photo_scenery, [i*160-x, 0])  # 背景は横に5回繰り返しで

        scene.blit(photo_chara[times%2], [224, 160])
        pygame.display.update()
        clock.tick(5)

if __name__== '__main__':
    game()


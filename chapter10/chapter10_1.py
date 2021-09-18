# pygameの使い方
import pygame  # pygameモジュールのインポート
import sys     # sysモジュールのインポート

WHITE = (250, 250, 250)  # 色の定義 白（色の指定は10進数のRGB値で行う）
BLACK = (0, 0, 0)        # 色の定義 黒
RED = (255, 0, 0)

# メイン処理を行う関数の定義
def game():
    pygame.init()                               # pygameモジュールの初期化（必須）
    pygame.display.set_caption("Pygameの基礎")   # ウィンドウのタイトルの指定
    scene = pygame.display.set_mode((800,600))  # 800x600の画面を生成
    clock = pygame.time.Clock()                 # clockオブジェクトを作成（プログラム内の時間管理に役立つ）
    font = pygame.font.Font(None, 200)          # fontオブジェクトを作成（pygameのフォントの設定）
    times = 0                                   # 時間を管理するtimes変数の宣言
    
    # 無限ループ
    while True:
        times = times + 1                  # timesの値を1増やす（時間のカウント）
        for event in pygame.event.get():   # pygameのイベントを繰り返しで処理する
            if event.type == pygame.QUIT:  # もし閉じるボタンが押されたら
                pygame.quit()              # pygameの終了
                sys.exit()                 # ウィンドウを閉じる

        texts = font.render(str(times), True, WHITE)  # render()命令で文字列と色を指定
        scene.fill(RED)                               # 背景の色の設定
        scene.blit(texts, [300, 200])                 # blit()命令で文字を画面に貼り付け

        pygame.display.update()
        clock.tick(1)

if __name__ == '__main__':
    game()

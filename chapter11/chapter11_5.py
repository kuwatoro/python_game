import pygame
import sys

white = (255, 255, 255)
black = (  0,   0,   0)

imgBattle = pygame.image.load("sample/image/btlbg.png")    # 戦闘の背景画像の読み込み
imgMonstar = pygame.image.load("sample/image/enemy1.png")  # 敵キャラ画像の読み込み
mon_x = 440-imgMonstar.get_width()/2                       # 敵キャラ画像の横x座標
mon_y = 560-imgMonstar.get_height()                        # 敵キャラ画像の縦y座標

words = [""]*10     # 戦闘メッセージを入れるリストを10個作る
def start_words():  # メッセージを空にする関数
    for m in range(10):  # 繰り返しでwordsリストに空の文字列を代入
        words[m] = ""

def set_words(wod):  # 🟨 文字列をセット 53行目の押されたキーのデータを受け取る
    for m in range(10):
        if words[m] == "":  # 文字列が入っていないリストがあれば、
            words[m] = wod  # 文字列をセットする
            return          # 17行目の関数の処理から戻る
    for m in range(9):
        words[m] = words[m+1]                                                                         
    words[9] = wod             # 新しく入力した文字は10行目に表示

def create_text(scn, fnt, x, y, txt, iro):  # 🟦 影付きの文字を描く（黒い文字の上に白い文字を描くことで影がついているように見せる）
    text = fnt.render(txt, True, black)
    scn.blit(text, [x+1, y+2])  # 黒い文字（影）は指定した座標より少し右下に描く
    text = fnt.render(txt, True, iro)
    scn.blit(text, [x, y])      # 白い文字はそのまま指定した座標に描く

def create_battle(scn, fnt):  # 🟥 実際に戦闘画面を描く
    scn.blit(imgBattle, [0, 0])           # 背景画像を配置
    scn.blit(imgMonstar, [mon_x, mon_y])  # 10、11行目で決めた座標に敵キャラ画像を配置
    for t in range(10):                   # 繰り返しで10行までメッセージを表示
        create_text(scn, fnt, 600, 100+t*50, words[t], white)  # 🟦 26行目に渡す words[t]は13行目で使用しているもの

def start_game():
    pygame.init()
    pygame.display.set_caption("敵のセリフ")
    scene = pygame.display.set_mode((880, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)

    start_words()

    while True:
        for rpg in pygame.event.get():
            if rpg.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if rpg.type == pygame.KEYDOWN:  # キーを押すイベントが発生した時
                set_words("KEYDOWN" + str(rpg.key))  # キーの値（SPACEなど）をメッセージに追加する
                                                     # 🟨 17行目に渡す
        create_battle(scene, font)  # 🟥 32行目に渡す
        pygame.display.update()
        clock.tick(5)
  
if __name__ == '__main__':
    start_game()

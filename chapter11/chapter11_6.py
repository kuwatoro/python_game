import pygame
import sys
import random
from pygame.locals import *

Azure = (240, 255, 255)  # 白 Azure	
Dsg   = (47, 79, 79)     # 黒 DarkSlateGray	

imgBattle = pygame.image.load("sample/image/btlbg.png")     # 戦闘の背景画像
imgEffect = pygame.image.load("sample/image/effect_a.png")  # 攻撃エフェクトの画像
imgMonstar = pygame.image.load("sample/image/enemy3.png")   # 敵キャラの画像
mon_x = 440 -imgMonstar.get_width()/2  # 敵キャラ画像のx座標
mon_y = 560 -imgMonstar.get_height()   # 敵キャラ画像のy座標
mon_move = 0     # 敵キャラを手前に移動するための変数
mon_flash = 0    # 敵キャラを点滅させる変数
field_shake = 0  # 画面を揺らすための変数
ORDER = ["[A]ttack", "[P]otion", "[B]laze gem", "[R]un"]  # 戦闘コマンドをリストで定義

words = [""]*10  # メッセージを入れるリストを10個作る
def start_words():       #  wordsリストを空にする関数
    for w in range(10):
        words[w] = ""     # 空の文字列をwordsリストに代入

def set_words(wod):  # 🟨 メッセージをセットする関数
    for w in range(10):
        if words[w] == "":  # メッセージがセットされていないリストがあれば
            words[w] = wod  # 新しいメッセージを代入
            return          # 24行目の関数の処理に戻り、29行目の関数へ
    for  w in range(9):
        words[w] = words[w+1]  # リストに振られてるメッセージの添字を一つずつずらす
    words[9] = wod             # 新しく10行目に文字列を表示

def create_text(scn, fnt, x, y, txt, iro):  # 🟦 右側に影付きの文字列を描く関数（戦闘コマンドとメッセージ）
    text = fnt.render(txt, True, Dsg)  # 黒い文字（影）
    scn.blit(text, [x+2, y+3])          # 影に見えるように白い文字から少しずらす
    text = fnt.render(txt, True, iro)  # 白い文字
    scn.blit(text, [x, y])              # 指定した位置に白い文字を配置

def create_battle(scn, fnt):  # 🟥
    global mon_flash, field_shake  # 敵を点滅させる、画面を揺らす変数を定義
    x = 0
    y = 0
    if field_shake > 0:  # 敵が攻撃してきた時、画面を揺らす
        field_shake = field_shake -1
        x = random.randint(-20, 20)
        y = random.randint(-10, 10)
    scn.blit(imgBattle, [x, y])
    if mon_flash %2 == 0:  # 敵を攻撃した時、点滅
        scn.blit(imgMonstar, [mon_x, mon_y + mon_move])
    if mon_flash > 0:
        mon_flash = mon_flash -1
    for w in range(10):  # 攻撃した後、戦闘メッセージを右側に配置
        create_text(scn, fnt, 600, 100+(w*50), words[w], Azure)  # 🟦 

def create_order(scn, fnt):  # 🟩 戦闘コマンドを左側に配置
    for o in range(4):
        create_text(scn, fnt, 20, 360+(60*o), ORDER[o], Azure)  # 🟦

def game():  # メインの処理を行う関数
    global mon_move, mon_flash, field_shake
    index = 10  # ゲーム進行を管理するインデックス 82行目戦闘開始から始めるので10にしておく
    timer = 0   # ゲーム進行を管理するタイマー 時間が経過するごとにカウントされる

    pygame.init()
    pygame.display.set_caption("決闘！！")
    scene = pygame.display.set_mode((880, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)

    start_words()

    while True:
        for rpg in pygame.event.get():
            if rpg.type == QUIT:
                pygame.quit()
                sys.exit()

        create_battle(scene, font)  # 🟥 戦闘画面を描画
        timer = timer +1             # timerを1増やす whileの無限ループで続いているので勝手に増えていく
        btn = pygame.key.get_pressed()
    
        if index == 10:  # ①戦闘開始
            if timer == 1: set_words("monster are here!")  # 🟨 タイマーが1になったら24行目に渡す
            if timer == 6:  # タイマーが6溜まったら
                index = 11  # 次のindex11に移行
                timer = 0   # タイマーを0にリセット

        elif index == 11: # ②プレイヤーの入力待ち
            if timer == 1: set_words("your turn")  # 🟨  タイマーが1になったら24行目に渡す
            create_order(scene, font)  # 🟩 game関数の中にあるのでscnではなく、scene
            if btn[K_a] == 1 or btn[K_SPACE] == 1:  # Aもしくはスペースが押されたら
                index = 12                          # 次のindex12に移行
                timer = 0                           # timerを0にリセット

        elif index == 12:  # ③プレイヤーの攻撃
            if timer == 1: set_words("you attack!")
            if 2 <= timer and timer <= 4:  # timerが2~4なら
                scene.blit(imgEffect, [700-(timer*120), -100+timer*120])
            if timer == 5:  # timerが5になったら
                mon_flash = 5
                set_words("**damage to monster!")
            if timer == 16:  # timerが16になったら
                index = 13   # 次のindex13に移行
                timer = 0    # timerを0にリセットする

        elif index == 13:  # ④敵のターン、敵の攻撃
            if timer == 1: set_words("monster turn")
            if timer == 5: # timerが5になったら
                set_words("monster attack!")
                mon_move = 30
            if timer == 9:
                set_words("**damage to player!")
                field_shake = 5
                mon_move = 0
            if timer == 20:  # timerが20になったら
                index = 11   # プレイヤーの入力待ちまで戻る
                timer = 0    # timerをリセット

        pygame.display.update()  
        clock.tick(5)

if __name__ == '__main__':
    game()

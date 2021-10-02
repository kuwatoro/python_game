import pygame
import sys

white = (255, 255, 255)

photoBattle = pygame.image.load("sample/image/btlbg.png")
photoMonstar = None

monstar_num = 0
monstar_x = 0
monstar_y = 0

def start_battle():
    global photoMonstar, monstar_num, monstar_x, monstar_y
    monstar_num = monstar_num +1
    if monstar_num == 5:
        monstar_num = 1
    photoMonstar = pygame.image.load("sample/image/enemy" + str(monstar_num) + ".png")
    monstar_x = 440-photoMonstar.get_width()/2
    monstar_y = 560-photoMonstar.get_height()

def create_battle(scn, fnt):  # ⭐️ 44行目から受け取る
    scn.blit(photoBattle, [0, 0])
    scn.blit(photoMonstar, [monstar_x, monstar_y])  # 19,20行目で指定した座標に敵キャラを配置
    info = fnt.render("sample/image/enemy" + str(monstar_num) + ".png", True, white)
    scn.blit(info, [280, 580])

def start_game():
    pygame.init()
    pygame.display.set_caption("戦闘開始！")
    scene = pygame.display.set_mode((880, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    start_battle()

    while True:
        for rpg in pygame.event.get():
            if rpg.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if rpg.type == pygame.KEYDOWN:
                if rpg.key == pygame.K_SPACE:
                    start_battle()

        create_battle(scene, font)  # ⭐️ 22行目に受け渡す
        pygame.display.update()
        clock.tick(5)

if __name__ == '__main__':
    start_game()
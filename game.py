import pygame
from random import *

#############################################################
# 기본 초기화 ( 반드시 해야 하는 것들 )
pygame.init()  # 초기화

# 화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면타이틀 설정
pygame.display.set_caption("Avoid Poop")  # 게임이름

# FPS
clock = pygame.time.Clock()
#############################################################

# 1. 사용자 게임 초기화 ( 배경화면, 게임 이미지, 좌표, 속도, 폰트 .. )

background = pygame.image.load("/Users/hanseung-won/PycharmProjects/Avoid Poop /background.png")
sprite = pygame.image.load("/Users/hanseung-won/PycharmProjects/Avoid Poop /sprite.png")
sprite_size = sprite.get_rect().size
sprite_width = sprite_size[0]
sprite_height = sprite_size[1]
sprite_x_pos = 0
sprite_y_pos = screen_height - sprite_height

# 이동할 좌표
to_x = 0

# 이동속도
sprite_speed = 0.5

poop = pygame.image.load("/Users/hanseung-won/PycharmProjects/Avoid Poop /poop.png")
poop_size = poop.get_rect().size  # 이미지의 크기를 구해옴
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_x_pos = randint(0, screen_width - poop_width)
poop_y_pos = 0
poop_speed = 0.5

game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성(폰트,크기), None = 디폴트 폰트

running = True  # 게임의 진행 여부
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정(30)

    # 2. 이벤트 처리 ( 키보드, 마우스 .. )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트
            running = False
        if event.type == pygame.KEYDOWN:  # 키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= sprite_speed
            elif event.key == pygame.K_RIGHT:
                to_x += sprite_speed
        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    sprite_x_pos += to_x * dt
    poop_y_pos += poop_speed * dt

    if poop_y_pos > screen_height:
        poop_x_pos = randint(0, screen_width - poop_width)
        poop_y_pos = 0

    # 가로 경계값 처리
    if sprite_x_pos < 0:
        sprite_x_pos = 0
    elif sprite_x_pos > screen_width - sprite_width:
        sprite_x_pos = screen_width - sprite_width

    # 4. 충돌 처리
    sprite_rect = sprite.get_rect()
    sprite_rect.left = sprite_x_pos
    sprite_rect.top = sprite_y_pos

    poop_rect = poop.get_rect()
    poop_rect.left = poop_x_pos
    poop_rect.top = poop_y_pos


    # 충돌 체크
    if poop_rect.colliderect(sprite_rect):  # 사각형기준으로 충돌이 있는지 확인하는 함수
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(sprite, (sprite_x_pos, sprite_y_pos))
    screen.blit(poop, (poop_x_pos, poop_y_pos))
    #screen.blit(game_over, (screen_width / 2, screen_height / 2))
    pygame.display.update()  # 게임화면을 계속 그리기


pygame.display.update()  # 게임화면을 계속 그리기
pygame.time.delay(2000)  # 2초 정도 대기 (2000ms)
pygame.quit()

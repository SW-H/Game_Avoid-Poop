import pygame
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
character = pygame.image.load("")
running = True  # 게임의 진행 여부
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정(30)

    # 2. 이벤트 처리 ( 키보드, 마우스 .. )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트
            running = False

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    pygame.display.update()  # 게임화면을 계속 그리기


pygame.quit()
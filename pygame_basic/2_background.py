import pygame

# 화면 크기 설정
screen_width = 480 # width
screen_height = 640 # height
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("웅겹살의 오락실게임") # 화면설정 screen변수로 선언

# 배경 이미지 불러오기
background = pygame.image.load("C:/PythonWorkspace/pygame_basic/background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생했는가? [사용자 event가 들어오는지 확인하는 로직.]
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생했는가?
            running = False             # 게임이 진행중이 아님

    screen.fill((33, 155, 155)) # RGB값으로도 배경 채울수 있다. fill 활용
    #screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update() # 게임화면 다시 그리기(필수)

# pygame QUIT
pygame.quit
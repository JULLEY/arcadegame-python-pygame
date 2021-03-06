import pygame

# 화면 크기 설정
screen_width = 480 # width
screen_height = 640 # height
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("웅겹살의 오락실게임") # 화면설정 screen변수로 선언

# 배경 이미지 불러오기
background = pygame.image.load("C:/PythonWorkspace/pygame_basic/background.png")

# 캐릭터(sprite) 불러오기
character = pygame.image.load("C:/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size                      # 이미지 크기를 구해옴
character_width = character_size[0]                             # 캐릭터의 가로크기
character_height = character_size[1]                            # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)    # 화면 가로의 중간위치
character_y_pos = screen_height - character_height              # 화면 세로 가장 하단

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생했는가? [사용자 event가 들어오는지 확인하는 로직.]
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생했는가?
            running = False             # 게임이 진행중이 아님

    screen.blit(background, (0, 0))                            # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면 다시 그리기(필수)

# pygame QUIT
pygame.quit
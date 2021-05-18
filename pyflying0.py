import pygame

WHITE = (255,255,255) # 흰색 표현 값 (R,G,B)
pad_w = 1024 #게임판 폭 전역변수
pad_h = 512 #게임판 높이 전역변수

def back(x,y):
    global gamepad, background
    gamepad.blit(background,(x,y))

def airplane(x,y): # 비행기의 게임판 위치
    global gamepad, aircraft
    gamepad.blit(aircraft,(x,y))

def runGame(): #실제 구동 함수
    global gamepad, clock, aircraft

    x = pad_w * 0.05
    y = pad_h * 0.8
    y_change = 0

    background_x = 0

    crashed = False #게임 종료를 위한 플래그
    while not crashed: 
        for event in pygame.event.get(): # 게임에서 발생하는 이벤트 리턴
            if event.type == pygame.QUIT: #마우스로 창을 닫으면 while문 탈
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change -= 5
                elif event.key == pygame.K_DOWN:
                    y_change += 5
            if event.type == pygame.KEYUP: # 키를 놓으면 움직임이 없도
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        y += y_change #키보드 입력에 따라 비행기의 y좌표 변경

        gamepad.fill(WHITE)
        back(background_x,0)
        airplane(x,y) # 게임판에 새로 그리기 위해 airplane 호출
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()

def initGame(): #초기화 함수
    global gamepad, clock,aircraft, background # 전역변수 사용 선언
    
    pygame.init() #pygame 사용을 위한 초기화
    
    gamepad = pygame.display.set_mode((pad_w,pad_h)) #게임판 크기 선언
    pygame.display.set_caption('PyFlying') #게임 타이틀 지정
    aircraft = pygame.image.load('C:/Users/user/Desktop/image/plane.png')
    background = pygame.image.load('C:/Users/user/Desktop/image/background.png')
    
    clock = pygame.time.Clock() #초당 프레임 설정
    runGame()

initGame()

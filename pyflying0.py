
import pygame
import random
from time import sleep

WHITE = (255,255,255) # 흰색 표현 값 (R,G,B)
RED = (255,0,0) # 빨간색 표현 값

pad_w = 1024 #게임판 폭 전역변수
pad_h = 512 #게임판 높이 전역변수
background_width = 1024
bat_width = 110
aircraft_width = 90
aircraft_height = 55

bat_width = 110
bat_height = 67


fireball1_width = 140
fireball1_height = 60
fireball2_width = 86
fireball2_height = 60

def drawScore(count):
    global gamepad

    font = pygame.font.SysFont(None,25)
    text = font.render('Bat Passed: '+ str(count),True,WHITE)
    gamepad.blit(text,(0,0))

def gameOver(): #박쥐를 3마리 놓치면 호출되는 함수
    global gamepad
    dispMessage('Game Over')

def textObj(text,font): # 게임화면에 표시될 텍스트 모양과 영역
    textSurface = font.render(text,True,RED)
    return textSurface, textSurface.get_rect()

def dispMessage(text):
    global gamepad

    #largeText = pygame.font.Font('freesansbold.ttf',115)
    largeText = pygame.font.SysFont("notosanscjkkr",115)
    TextSurt, TextRect = textObj(text,largeText)
    TextRect.center = ((pad_w/2),(pad_h/2))
    gamepad.blit(TextSurt,TextRect) # 빨간색으로 crash 출력
    pygame.display.update()
    sleep(2) # 2초 쉬고 다시 게임 시작
    runGame()

def crash():
    global gamepad
    dispMessage('Crashed!')

def drawobject(obj,x,y): # 게임판에 그려지는 객체
    global gamepad
    gamepad.blit(obj,(x,y))


def runGame(): #실제 구동 함수
    global gamepad, clock, aircraft, background1,background2
    global bat, fires, bullet, boom

    isShotBat = False # 총알이 박쥐를 명중했는지 안했는지 판단하기 위한 플래그
    boom_count = 0 # 폭발 이미지가 화면에 표시되는 시간을 위한 변수

    bat_passed = 0
    
    bullet_xy = []
    
    x = pad_w * 0.05
    y = pad_h * 0.8
    y_change = 0

    background1_x = 0 # 배경 이지이 위치
    background2_x = background_width # 복사본은 원본 바로 다음 위치로 좌표 선택

    bat_x = pad_w # 박쥐 날아올 위치 x 게임판의 맨 오른쪽 끝으로 
    bat_y = random.randrange(0,pad_h) # 박쥐 날아올 위치 y 게임판 높이범위에서 무작위

    fire_x = pad_w # 불덩이도 마찬가지로 박쥐처럼 등장
    fire_y = random.randrange(0,pad_h)
    random.shuffle(fires) # fires 무작위로 섞은 후 첫번째 발사
    fire = fires[0] # 5개 원소 중 2개가 불덩이 
    
    crashed = False #게임 종료를 위한 플래그
    while not crashed: 
        for event in pygame.event.get(): # 게임에서 발생하는 이벤트 리턴
            if event.type == pygame.QUIT: #마우스로 창을 닫으면 while문 탈
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

                elif event.key == pygame.K_LEFT:
                    bullet_x = x + aircraft_width
                    bullet_y = y + aircraft_height/2
                    bullet_xy.append([bullet_x,bullet_y])

                               
            if event.type == pygame.KEYUP: # 키를 놓으면 움직임이 없도
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        # clear gamepad
        gamepad.fill(WHITE)

        # draw background
        background1_x -= 2 # 배경 2픽셀 만큼 왼쪽으로 이동
        background2_x -= 2

        # 배경 이미지가 완전히 사라지면 그 위치를 배경 이미지 복사본 오른쪽으로
        if background1_x == -background_width:
            background1_x = background_width
        if background2_x == -background_width:
            background2_x = background_width
            

        drawobject(background1,background1_x,0)
        drawobject(background2, background2_x,0)

        drawScore(bat_passed)

        # 박쥐가 3번 이상 넘어가면 게임오버
        if bat_passed > 2:
            gameOver()
            
        
        y += y_change #키보드 입력에 따라 비행기의 y좌표 변경
        if y < 0:
            y = 0
        elif y > pad_h - aircraft_height:
            y = pad_h - aircraft_height
        
        # Bat position

        bat_x -= 7 # 비행기 쪽으로 7 픽셀씩 날아오게 
        if bat_x <=0: # 왼쪽 끝까지 날아가면 다시 위치 잡기
            bat_passed += 1 #박쥐가 화면 왼쪽에 도달하면 1 증
            bat_x = pad_w
            bat_y = random.randrange(0,pad_h)

        # Fire position
        if fire[1] == None: # 아무런 방해물이 없는 것
            fire_x -= 30
        else: # 방해물 있을 때 15픽셀씩 날아오게 하
            fire_x -= 15

        if fire_x <= 0:
            fire_x = pad_w
            fire_y = random.randrange(0,pad_h)
            random.shuffle(fires)
            fire = fires[0]
        # Bullets Position

        if len(bullet_xy) != 0:
            for i,bxy in enumerate(bullet_xy):
                bxy[0] += 15
                bullet_xy[i][0] = bxy[0]
                
                if bxy[0] < bat_x:
                    if bxy[1] > bat_y and bxy[1] < bat_y + bat_height:
                        bullet_xy.remove(bxy) # 화면에서 총알 제거하기 위해
                        isShotBat = True
                        
                if bxy[0] >= pad_w:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass
                    
        if x+aircraft_width > bat_x: #비행기가 박쥐와 충돌 했는지
            if (y >bat_y and y < bat_y+bat_height) or (y+aircraft_height > bat_y and y+aircraft_height < bat_y+bat_height):
                crash()
        # 비행기와 불덩이가 충돌했는지 체크
        if fire[1] != None:
            if fire[0] == 0: # 첫번째 불덩이라면
                fireball_width = fireball1_width
                fireball_height = fireball1_height
            elif fire[0] == 1: # 두번째 불덩이라
                fireball_width = fireball2_width
                fireball_height = fireball2_height
            if x+aircraft_width > fire_x:
                if(y+aircraft_height > fire_y and y+aircraft_height < fire_y+ fireball_height):
                    crash()
                    
        drawobject(aircraft,x,y)

        if len(bullet_xy)!=0: 
            for bx,by in bullet_xy:
                drawobject(bullet,bx,by)

        if not isShotBat: #총알이 박쥐에 명중하지 않았다면 박쥐를 계속 그려줌
            drawobject(bat,bat_x,bat_y)
        else:
            drawobject(boom,bat_x,bat_y)
            boom_count += 1
            if boom_count > 5:
                boom_count = 0
                bat_x = pad_w
                bat_y = random.randrange(0,pad_h-bat_height)
                isShotBat= False
        
        if fire[1] != None:
            drawobject(fire[1],fire_x,fire_y)
        
        
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()

def initGame(): #초기화 함수
    global gamepad, clock,aircraft, background1,background2 # 전역변수 사용 선언
    global bat, fires, bullet, boom

    fires = [] # 방해요소
    
    pygame.init() #pygame 사용을 위한 초기화
    
    gamepad = pygame.display.set_mode((pad_w,pad_h)) #게임판 크기 선언
    pygame.display.set_caption('PyFlying') #게임 타이틀 지정
    aircraft = pygame.image.load('C:/Users/user/Desktop/image/plane.png')
    background1 = pygame.image.load('C:/Users/user/Desktop/image/background.png')
    background2 = background1.copy() # 복사본 할당
    bat = pygame.image.load('C:/Users/user/Desktop/image/bat.png')
    fires.append((0,pygame.image.load('C:/Users/user/Desktop/image/fireball.png'))) #리스트 변수 fires를 (숫자, 이미지) 변경
    fires.append((1,pygame.image.load('C:/Users/user/Desktop/image/fireball2.png')))

    boom = pygame.image.load('C:/Users/user/Desktop/image/boom.png') # 박쥐가 터지는 장면

    for i in range(3):
        fires.append((i+2,None))
    bullet = pygame.image.load('C:/Users/user/Desktop/image/bullet.png')
    
    clock = pygame.time.Clock() #초당 프레임 설정
    runGame()

if __name__ == '__main__':
    initGame()

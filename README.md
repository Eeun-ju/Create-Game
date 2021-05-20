# Create-Game

### 기초적인 파이썬 게임 제작하기
 파이썬으로 게임을 만들 수 있다고 해서 해보는 프로젝트!  
 참고자료 소스를 따라가며 코드와 진행 방식을 이해해보자 
   
 
 첫 번째 게임 : PyFlying(비행기 미니 게임)  
 게임 방법 : 비행기가 날아오는 불덩이를 피하면서 박쥐를 파괴하는 게임으로, 연속으로 박쥐를 세 번 맞추지 못하면 게임이 종료된다.
   
    #참고자료 코드 변경 부분
    elif event.key == pygame.K_LCTRL -> elif event.key == pygame.K_LEFT
    
    largeText = pygame.font.Font('freesansbold.ttf',115) -> largeText = pygame.font.SysFont("notosanscjkkr",115)
 
 
<h5> 참고자료 : https://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220706335386&parentCategoryNo=&categoryNo=80&viewDate=&isShowPopularPosts=true&from=search

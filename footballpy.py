import pygame, sys, os
from pygame.math import Vector2
FPS = 60
pygame.init()
screen_width = 1250
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
game_icon = pygame.image.load(os.path.join ('support', 'gameicon.png')).convert_alpha()
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Football")
clock = pygame.time.Clock()
fullscreen = False
#game font
game_font = pygame.font.Font(os.path.join ('support','freesansbold.ttf'), 32)

#sounds
ball_hit = pygame.mixer.Sound(os.path.join ('support', "ball_hit.wav"))
score_m = pygame.mixer.Sound(os.path.join ('support',"score.wav"))
boo = pygame.mixer.Sound(os.path.join ('support',"boo.wav"))
player_hit = pygame.mixer.Sound(os.path.join ('support',"ball_hitr.wav"))

#background
background = pygame.image.load(os.path.join ('support', 'BG_IMG.png')).convert()
player1_goal = pygame.Rect(5, screen_height/2-82, 10, 170)
player2_goal = pygame.Rect(screen_width-15, screen_height/2-82, 10, 170)

#player1
player1 = pygame.image.load(os.path.join ('support','player1.png')).convert_alpha()
player1_player = player1
player1_angle = 0
player1_velocity = Vector2(-3,0)
player1_position = Vector2(screen_width/2+300, screen_height/2-50)
player1_rect = player1.get_rect(center = player1_position)
player1_mask = pygame.mask.from_surface(player1)
player1_score = 0
play1_stext = game_font.render("player1 ", False, (200, 200, 200))

#player2
player2 = pygame.image.load(os.path.join ('support','player2.png')).convert_alpha()
player2_player = player2
player2_angle = 0
player2_velocity = Vector2(3,0)
player2_position = Vector2(screen_width/2-300, screen_height/2+50)
player2_rect = player2.get_rect(center = player2_position)
player2_mask = pygame.mask.from_surface(player2)
player2_score = 0
play2_stext = game_font.render("player2 ", False, (200, 200, 200))

#ball
ball = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.draw.circle(ball, [255, 255, 255], [15, 15], 15)
ball_vel = Vector2(0, 0)
ball_pos = Vector2(screen_width/2, screen_height/2)
ball_rect = ball.get_rect(center = ball_pos)
ball_mask = pygame.mask.from_surface(ball)
        
run = False
pause = False
main = True
while main == True:        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    if event.type == pygame.KEYDOWN:
        main = False
        run = True
        if event.key == pygame.K_f:
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
    mainscreen = pygame.image.load(os.path.join ('support','main_screen.png')).convert()
    screen.blit(mainscreen,(0,0))
    pygame.display.flip()
    clock.tick(10)
    
while run == True:
    pygame.mixer.unpause()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            run=False
                   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        player1_angle +=5
        player1_velocity.rotate_ip(-5)
        player1_player = pygame.transform.rotate(player1, player1_angle)
        player1_rect = player1_player.get_rect(center = player1_rect.center)
        player1_mask = pygame.mask.from_surface(player1_player)
                        
    elif keys[pygame.K_UP]:
        player1_angle -=5
        player1_velocity.rotate_ip(5)
        player1_player = pygame.transform.rotate(player1, player1_angle)
        player1_rect = player1_player.get_rect(center = player1_rect.center)
        player1_mask = pygame.mask.from_surface(player1_player)

    if keys[pygame.K_LEFT]:
        player1_angle +=5
        player1_velocity.rotate_ip(-5)
        player1_player = pygame.transform.rotate(player1, player1_angle)
        player1_rect = player1_player.get_rect(center = player1_rect.center)
        player1_mask = pygame.mask.from_surface(player1_player)
                        
    elif keys[pygame.K_RIGHT]:
        player1_angle -=5
        player1_velocity.rotate_ip(5)
        player1_player = pygame.transform.rotate(player1, player1_angle)
        player1_rect = player1_player.get_rect(center = player1_rect.center)
        player1_mask = pygame.mask.from_surface(player1_player)

    if keys[pygame.K_w]:
        player2_angle +=5
        player2_velocity.rotate_ip(-5)
        player2_player = pygame.transform.rotate(player2, player2_angle)
        player2_rect = player2_player.get_rect(center = player2_rect.center)
        player2_mask = pygame.mask.from_surface(player2_player)
                        
    elif keys[pygame.K_s]:
        player2_angle -=5
        player2_velocity.rotate_ip(5)
        player2_player = pygame.transform.rotate(player2, player2_angle)
        player2_rect = player2_player.get_rect(center = player2_rect.center)
        player2_mask = pygame.mask.from_surface(player2_player)

    if keys[pygame.K_a]:
        player2_angle +=5
        player2_velocity.rotate_ip(-5)
        player2_player = pygame.transform.rotate(player2, player2_angle)
        player2_rect = player2_player.get_rect(center = player2_rect.center)
        player2_mask = pygame.mask.from_surface(player2_player)
                        
    elif keys[pygame.K_d]:
        player2_angle -=5
        player2_velocity.rotate_ip(5)
        player2_player = pygame.transform.rotate(player2, player2_angle)
        player2_rect = player2_player.get_rect(center = player2_rect.center)
        player2_mask = pygame.mask.from_surface(player2_player)

    if keys[pygame.K_SPACE]:
        pause = True
        pygame.mixer.pause()

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        ball_vel = Vector2(0, 0)
        ball_pos = Vector2(screen_width/2, screen_height/2)
        pygame.mixer.Sound.play(boo)
    current_time = pygame.time.get_ticks()
    player1_position += player1_velocity
    player1_rect.center = player1_position
    player2_position += player2_velocity
    player2_rect.center = player2_position
    ball_vel *= 0.99
    ball_pos += ball_vel
    ball_rect.center = ball_pos

    player1_offset = player1_rect[0] -ball_rect[0], player1_rect[1] -ball_rect[1]
    player1_overlap = ball_mask.overlap(player1_mask, player1_offset)

    player2_offset = player2_rect[0] -ball_rect[0], player2_rect[1] -ball_rect[1]
    player2_overlap = ball_mask.overlap(player2_mask, player2_offset)

    if player1_overlap:
        ball_vel = Vector2(player1_velocity) *1.4
        pygame.mixer.Sound.play(ball_hit)
        
    if player2_overlap:
        ball_vel = Vector2(player2_velocity) *1.4
        pygame.mixer.Sound.play(ball_hit)
        
    if player1_overlap and player2_overlap:
        player1_overlap = None
        player2_overlap = None
        ball_vel *= 0
        
    if ball_pos[0]>= screen_width-25 or ball_pos[0]<= 25 or ball_pos[1]>= screen_height-30 or ball_pos[1]<= 30:
        pygame.mixer.Sound.play(ball_hit)

    if ball_pos[0]>= screen_width-25:
        ball_pos[0] = screen_width-26
        ball_vel *= -0.99  
    if ball_pos[0]<= 25:
        ball_pos[0] = 26
        ball_vel *= -0.99
    if ball_pos[1]>= screen_height-30:
        ball_pos[1] = screen_height-31
        ball_vel *= -0.99
    if ball_pos[1]<= 30:
        ball_pos[1] = 31
        ball_vel *= -0.99
            
    if player1_position[0]>= screen_width-25 or player1_position[0]<= 25 or player1_position[1]>= screen_height-25 or player1_position[1]<= 25:
        player1_velocity = -player1_velocity
        pygame.mixer.Sound.play(player_hit)
        #or player1_velocity = pygame.math.Vector2.reflect(player1_velocity, player1_velocity)
                
    if player2_position[0]>= screen_width-25 or player2_position[0]<= 25 or player2_position[1]>= screen_height-25 or player2_position[1]<= 25:
        player2_velocity = -player2_velocity
        pygame.mixer.Sound.play(player_hit)

    if ball_rect.colliderect(player1_goal):
        player1_score += 1
        ball_vel = Vector2(0, 0)
        ball_pos = Vector2(screen_width/2, screen_height/2)
        play1_stext = game_font.render(f"player1 {player1_score}", False, (200, 200, 200))
        pygame.mixer.Sound.play(score_m)
        
    if ball_rect.colliderect(player2_goal):
        player2_score += 1
        ball_vel = Vector2(0, 0)
        ball_pos = Vector2(screen_width/2, screen_height/2)
        play2_stext = game_font.render(f"player2 {player2_score}", False, (200, 200, 200))
        pygame.mixer.Sound.play(score_m)
        
    while pause == True:
        for event in pygame.event.get():
            pause_text = game_font.render(f"press a key to continue", False, (255, 255, 255))
            screen.blit(pause_text,(screen_width/2-180, screen_height/2))
            pygame.display.flip()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pause = False
                                      
    screen.blit(background,(0,0))
    #pygame.draw.rect(screen, (200, 200, 200), player1_goal)
    #pygame.draw.rect(screen, (200, 200, 200), player2_goal)
    screen.blit(play2_stext,(100,15))
    screen.blit(play1_stext,(995,15))
    screen.blit(ball, ball_rect)
    screen.blit(player1_player, player1_rect)
    screen.blit(player2_player, player2_rect)
    pygame.display.flip()
    clock.tick(FPS)

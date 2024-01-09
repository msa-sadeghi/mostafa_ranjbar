# import pygame
# pygame.init()
# SCREEN_WIDTH = 1250
# SCREEN_HEIGHT = 700
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# FPS = 60
# clock = pygame.time.Clock()
# hourse_image = pygame.image.load("assets/h.png")
# hourse_rect = hourse_image.get_rect()
# hourse_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
# hourse_right_image = hourse_image
# hourse_left_image = pygame.transform.flip(hourse_right_image, True, False)
# score = 0
# font = pygame.font.Font("assets/Facon.ttf", 38)
# score_text = font.render(f"Score:{score}", True, (10,130,240))
# score_rect = score_text.get_rect()
# score_rect.topleft = (0,0)

# sound1 = pygame.mixer.Sound("assets/new_round.wav")
# pygame.mixer.music.load("assets/new_round.wav")
# pygame.mixer.music.play(-1)


# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         # if event.type == pygame.KEYDOWN:
#         #     if event.key == pygame.K_SPACE:
#         #         sound1.play()
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         hourse_rect.y -= 5
#     if keys[pygame.K_DOWN]:
#         hourse_rect.y += 5
#     if keys[pygame.K_LEFT]:
#         hourse_rect.x -= 5
#         hourse_image = hourse_left_image
#     if keys[pygame.K_RIGHT]:
#         hourse_rect.x += 5
#         hourse_image = hourse_right_image
#     screen.fill((120,1,130))
#     screen.blit(hourse_image, hourse_rect)
#     screen.blit(score_text, score_rect)
#     pygame.display.update()
#     clock.tick(FPS)
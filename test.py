import pygame

audio_path = "E:/bilibiliPlayer/audio/"

pygame.init()

pygame.display.set_mode((10, 10))

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

pygame.mixer.music.load(audio_path + "test.mp3")
pygame.mixer.music.play()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MUSIC_END:
            print('music end event')

        if event.type == pygame.MOUSEBUTTONDOWN:
            # play again
            pygame.mixer.music.play()

pygame.quit()
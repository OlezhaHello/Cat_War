

import time
from sprite import *


def dialogue_mode(sprite, text):
    sprite.update()
    screen.blit(space, (0, 0))
    screen.blit(sprite.image, sprite.rect)

    text1 = f1.render(text[text_number], True, pg.Color("white"))

    screen.blit(text1, (280, 450))
    if text_number < len(text) - 1:
        text2 = f1.render(text[text_number + 1], True, pg.Color("white"))
        screen.blit(text2, (280, 470))


pg.init()
pg.mixer.init()

size = (800, 600)
screen = pg.display.set_mode(size)
pg.display.set_caption("Космические коты")

FPS = 120
clock = pg.time.Clock()

is_running = True
mode = "start_scene"

meteorites = pg.sprite.Group()
mice = pg.sprite.Group()
lasers = pg.sprite.Group()

captain = Captain()
alien = Alien()
starship = Starship()

space = pg.image.load("space.png").convert()
space = pg.transform.scale(space, size).convert_alpha()

heart = pg.image.load("heart.png")
heart = pg.transform.scale(heart, (30, 30)).convert_alpha()
heart_count = 3

start_text = ["Мы засекли сигнал с планеты Мур.",
              "",
              "Наши друзья, инопланетные коты,",
              "нуждаются в помощи.",
              "Космические мыши хотят съесть их луну,",
              "потому что она похожа на сыр.",
              "Как долго наш народ страдал от них, ",
              "теперь и муряне в беде...",
              "Мы должны помочь им.",
              "Вылетаем прямо сейчас.",
              "Спасибо, что починил звездолёт, штурман. ",
              "Наконец-то функция автопилота работает.",
              "Поехали!"]

alien_text = ["СПАСИТЕ! МЫ ЕЛЕ ДЕРЖИМСЯ!",
              "",
              "Мыши уже начали грызть луну...",
              "Скоро куски луны будут падать на нас.",
              "Спасите муриан!", ]

final_text = ["Огромное вам спасибо,",
              "друзья с планеты Мяу!",
              "Как вас называть? Мяуанцы? Мяуриане?",
              "В любом случае, ",
              "теперь наша планета спасена!",
              "Мы хотим отблагодарить вас.",
              "Капитан Василий и его штурман получают",
              "орден SKYSMART.",
              "А также несколько бутылок нашей",
              "лучшей валерьянки.",
              "",
              ""]

text_number = 0
f1 = pg.font.Font("FRACTAL.otf", 25)

pg.mixer.music.load("Tense Intro.wav")
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play()

laser_sound = pg.mixer.Sound("11377 ice cannon shot.wav")
win_sound = pg.mixer.Sound("Victory Screen Appear 01.wav")

while is_running:

    # СОБЫТИЯ
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg.KEYDOWN:
            if mode == "start_scene":
                text_number += 2
                if text_number > len(start_text):
                    mode = "meteorites"
                    text_number = 0
                    start_time = time.time()
            if mode == "alien_scene":
                text_number += 2
                if text_number > len(alien_text):
                    mode = "moon"
                    starship.switch_mode()
                    text_number = 0
                    start_time = time.time()
            if mode == "moon":
                if event.key == pg.K_SPACE:
                    lasers.add(Laser(starship.rect.midtop))
                    laser_sound.play()
            if mode == "final_scene":
                text_number += 2
                if text_number >= len(final_text):
                    mode = "end"
                    text_number = 0
                    start_time = time.time()
                    is_running = False

    if mode == "start_scene":
        dialogue_mode(captain, start_text)

    if mode == "meteorites":
        if time.time() - start_time > 20.0:
            mode = "alien_scene"

        if random.randint(1, 80) == 1:
            meteorites.add(Meteorite())

        starship.update()
        meteorites.update()

        hits = pg.sprite.spritecollide(starship, meteorites, True)
        for hit in hits:
            heart_count -= 1
            if heart_count <= 0:
                is_running = False

        # ОТРИСОВКA
        screen.blit(space, (0, 0))
        screen.blit(starship.image, starship.rect)
        meteorites.draw(screen)

        for i in range(heart_count):
            screen.blit(heart, (i * 30, 0))

    if mode == "alien_scene":
        dialogue_mode(alien, alien_text)

    if mode == "moon":
        if time.time() - start_time > 20.0:
            mode = "final_scene"
            pg.mixer.music.fadeout(3)
            win_sound.play()

        if random.randint(1, 20) == 1:
            mice.add(Mouse_starship())

        starship.update()
        mice.update()
        lasers.update()

        hits = pg.sprite.spritecollide(starship, mice, True)
        for hit in hits:
            heart_count -= 1
            if heart_count <= 0:
                is_running = False

        hits = pg.sprite.groupcollide(lasers, mice, True, True)
        for hit in hits:
            ...

        screen.blit(space, (0, 0))
        screen.blit(starship.image, starship.rect)
        mice.draw(screen)
        lasers.draw(screen)

        for i in range(heart_count):
            screen.blit(heart, (i * 30, 0))

    if mode == "final_scene":
        dialogue_mode(alien, final_text)

    pg.display.flip()
    clock.tick(FPS)

























#
# import time
# from sprite import *
# import pygame as pg
#
# def dialogue_mode(sprite, text):
#     sprite.update()
#     screen.blit(space, (0, 0))
#     screen.blit(sprite.image, sprite.rect)
#
#     text1 = f1.render(text[text_number], True, pg.Color("White"))
#     screen.blit(text1, (250, 450))
#
#     if text_number < len(text) - 1:
#         text2 = f1.render(text[text_number + 1], True, pg.Color("White"))
#         screen.blit(text2, (250, 470))
#
#
#
# pg.init()
# pg.mixer.init()
#
# size = (800, 600)
# screen = pg.display.set_mode(size)
# pg.display.set_caption("Космические коты")
#
# FPS = 120
# clock = pg.time.Clock()
#
# is_running = True
# mode = "start_scene"
#
# meteorites = pg.sprite.Group()
# mice = pg.sprite.Group()
# lasers = pg.sprite.Group()
#
# captain = Captain()
# alien = Alien()
# starship = Starship()
#
# space=pg.image.load('space.png').convert()
# space=pg.transform.scale(space,size).convert_alpha()
# heart=pg.image.load('heart.png')
# heart=pg.transform.scale(heart,(30,30)).convert_alpha()
# heart_count=3
#
# start_text = ["Мы засекли сигнал с планеты Мур.",
#               "",
#               "Наши друзья, инопланетные коты,",
#               "нуждаются в помощи.",
#               "Космические мыши хотят съесть их луну,",
#               "потому что она похожа на сыр.",
#               "Как долго наш народ страдал от них, ",
#               "теперь и муряне в беде...",
#               "Мы должны помочь им.",
#               "Вылетаем прямо сейчас.",
#               "Спасибо, что починил звездолёт, штурман. ",
#               "Наконец-то функция автопилота работает.",
#               "Поехали!"]
#
# alien_text = ["СПАСИТЕ! МЫ ЕЛЕ ДЕРЖИМСЯ!",
#               "",
#               "Мыши уже начали грызть луну...",
#               "Скоро куски луны будут падать на нас.",
#               "Спасите муриан!",
#               " "
#               ]
#
# final_text = ["Огромное вам спасибо,",
#               "друзья с планеты Мяу!",
#               "Как вас называть? Мяуанцы? Мяуриане?",
#               "В любом случае, ",
#               "теперь наша планета спасена!",
#               "Мы хотим отблагодарить вас.",
#               "Капитан Василий и его штурман получают",
#               "орден SKYSMART.",
#               "А также несколько бутылок нашей",
#               "лучшей валерьянки.",
#               "",
#               ""]
#
# text_number = 0
# f1=pg.font.Font("FRACTAL.otf",25)
#
# first_time = True
# while is_running:
#
#     # СОБЫТИЯ
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             is_running = False
#         if event.type == pg.KEYDOWN:
#             if mode == "start_scene":
#                 text_number += 2
#                 if text_number > len(start_text):
#                     mode = "meteorites"
#                     text_number = 0
#                     start_time = time.time()
#         if mode == "alien_scene":
#             text_number += 2
#             if text_number > len(alien_text):
#                 mode = "moon"
#                 starship.switch_mode()
#                 text_number = 0
#                 start_time = time.time()
#         if mode == "moon":
#             if event.key == pg.K_SPACE:
#                 lasers.add(Laser(starship.rect.midtop))
#                 # laser_sound.play()
#         if mode == "final_scene":
#             text_number += 2
#             if text_number >= len(final_text):
#                 mode = "end"
#                 text_number = 0
#                 start_time = time.time()
#                 is_running = False
#     if mode == "start_scene":
#         dialogue_mode(captain,start_text)
#     if mode == "meteorites":
#         if time.time() - start_time > 20.0:
#             mode='alien_scene'
#         if random.randint(1,30)==1:
#             meteorites.add(Meteorite())
#
#         starship.update()
#         meteorites.update()
#         hits=pg.sprite.spritecollide(starship,meteorites,True)
#         for hit in hits:
#             heart_count-=1
#             if heart_count == 0:
#                 is_running = False
#         screen.blit(space,(0,0))
#         screen.blit(starship.image, starship.rect)
#         meteorites.draw(screen)
#         for i in range(heart_count):
#             screen.blit(heart,(i*30,0))
#     if mode == "alien_scene":
#         dialogue_mode(alien, alien_text)
#     if mode == 'moon':
#         for event in pg.event.get():
#             if event.key == pg.K_SPACE:
#                 lasers.add(Laser())
#
#
#     if mode == "moon":
#         if time.time() - start_time > 20.0:
#             mode = 'final_scene'
#         if random.randint(1, 30) == 1:
#             mice.add(Mouse_starship())
#
#         starship.update()
#         mice.update()
#         lasers.update()
#         hits = pg.sprite.spritecollide(starship, mice, True)
#         for hit in hits:
#             heart_count -= 1
#             if heart_count == 0:
#                 is_running = False
#         hits=pg.sprite.groupcollide(lasers,mice,True,True)
#         screen.blit(space, (0, 0))
#         screen.blit(starship.image, starship.rect)
#         mice.draw(screen)
#         lasers.draw(screen)
#
#     if mode == "final_scene":
#         dialogue_mode(alien, final_text)
#
#     pg.display.flip()
#     clock.tick(FPS)
#
#


# import time
# from sprite import *
# import pygame as pg
#
# def dialogue_mode(sprite, text):
#     sprite.update()
#     screen.blit(space, (0, 0))
#     screen.blit(sprite.image, sprite.rect)
#
#     text1 = f1.render(text[text_number], True , pg.Color('White'))
#     screen.blit(text1, (250, 450))
#
#     if text_number < len(text) - 1:
#         text2 = f1.render(text[text_number + 1 ], True, pg.Color('White'))
#         screen.blit(text2, (250, 470))
#
#
#
# pg.init()
# pg.mixer.init()
#
# size = (800, 600)
# screen = pg.display.set_mode(size)
# pg.display.set_caption("Космические коты")
#
# FPS = 120
# clock = pg.time.Clock()
#
# is_running = True
# mode = "start_scene"
#
# meteorites = pg.sprite.Group()
# mice = pg.sprite.Group()
# lasers = pg.sprite.Group()
# space=pg.image.load('space.png').convert()
# space=pg.transform.scale(space,size)
# heart=pg.image.load('heart.png').convert_alpha()
# heart=pg.transform.scale(heart,(30,30))
# heart_count=3
# captain = Captain()
# alien=Alien()
# starship=Starship()
#
# start_text = ["Мы засекли сигнал с планеты Мур.",
#               "",
#               "Наши друзья, инопланетные коты,",
#               "нуждаются в помощи.",
#               "Космические мыши хотят съесть их луну,",
#               "потому что она похожа на сыр.",
#               "Как долго наш народ страдал от них, ",
#               "теперь и муряне в беде...",
#               "Мы должны помочь им.",
#               "Вылетаем прямо сейчас.",
#               "Спасибо, что починил звездолёт, штурман. ",
#               "Наконец-то функция автопилота работает.",
#               "Поехали!"]
#
# alien_text = ["СПАСИТЕ! МЫ ЕЛЕ ДЕРЖИМСЯ!",
#               " ",
#               "Мыши уже начали грызть луну...",
#               "Скоро куски луны будут падать на нас.",
#               "Спасите муриан!",
#               " "
#               ]
#
# final_text = ["Огромное вам спасибо,",
#               "друзья с планеты Мяу!",
#               "Как вас называть? Мяуанцы? Мяуриане?",
#               "В любом случае, ",
#               "теперь наша планета спасена!",
#               "Мы хотим отблагодарить вас.",
#               "Капитан Василий и его штурман получают",
#               "орден SKYSMART.",
#               "А также несколько бутылок нашей",
#               "лучшей валерьянки.",
#               "",
#               ""]
#
# text_number = 0
# f1=pg.font.Font("FRACTAL.otf",25)
# first_time = True
# while is_running:
#
# # СОБЫТИЯ
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             is_running = False
#         if event.type == pg.KEYDOWN:
#             if mode == "start_scene":
#                 text_number += 2
#                 if text_number > len(start_text):
#                     mode = "meteorites"
#                     text_number = 0
#                     start_time = time.time()
#         if mode == "alien_scene":
#             text_number += 2
#             if text_number > len(alien_text):
#                 mode = "moon"
#                 starship.switch_mode()
#                 text_number = 0
#                 start_time = time.time()
#         if mode == "moon":
#             if event.key == pg.K_SPACE:
#                  lasers.add(Laser(starship.rect.midtop))
#                  # laser_sound=laser_sound.wav
#                  # laser_sound.play
#         if mode == "final_scene":
#             text_number += 2
#             if text_number >= len(final_text):
#                 mode = "end"
#                 text_number = 0
#                 start_time = time.time()
#                 is_running = False
# # while is_running:
# #
# #     # СОБЫТИЯ
# #     for event in pg.event.get():
# #         if event.type == pg.QUIT:
# #             is_running = False
# #         if event.type == pg.KEYDOWN:
# #             if mode == 'start_scene':
# #                 text_number+=2
# #                 if text_number > len(start_text):
# #                     text_number= 0
# #                     mode = 'meteorites'
# #                     start_time=time.time()
# #
# #
# #             if mode == 'alien_scene':
# #                 text_number+=2
# #
# #                 if text_number > len(alien_text):
# #
# #                     alien.rect.topleft = (-30, 600)
# #                     text_number = 0
# #                     alien.mode = "up"
# #                     mode = 'moon'
# #                     start_time=time.time()
# #                     starship.switch_mode()
# #
# #
# #             if mode == 'final_scene':
# #
# #                 text_number += 2
# #                 if text_number > len(alien_text):
# #                     text_number = 0
# #                 mode = 'end'
#
#     # ОБНОВЛЕНИЯ
#     if mode == "start_scene":
#         dialogue_mode(captain,start_text)
#     if mode == "meteorites":
#         if time.time() - start_time > 20.0:
#             mode='moon'
#         if random.randint(1,50)==1:
#             meteorites.add(Meteorite())
#
#         starship.update()
#         meteorites.update()
#         hits=pg.sprite.spritecollide(starship,meteorites,True)
#         for hit in hits:
#             heart_count-=1
#             if heart_count == 0:
#                 is_running=False
#         screen.blit(space,(0,0))
#         screen.blit(starship.image, starship.rect)
#         meteorites.draw(screen)
#         for i in range(heart_count):
#             screen.blit(heart,(i*30,0))
#     if mode == "alien_scene":
#         dialogue_mode(alien, alien_text)
#     if mode == 'moon':
#         for event in pg.event.get():
#             if event.key == pg.K_SPACE:
#                 lasers.add(Laser())
#
#
#     if mode == "moon":
#         if time.time() - start_time > 20.0:
#             mode = 'final_scene'
#         if random.randint(1, 30) == 1:
#             mice.add(Mouse_starship())
#
#         starship.update()
#         mice.update()
#         lasers.update()
#         hits = pg.sprite.spritecollide(starship, mice, True)
#         for hit in hits:
#             heart_count -= 1
#             if heart_count == 0:
#                 is_running = False
#         hits=pg.sprite.groupcollide(lasers,mice,True,True)
#         screen.blit(space, (0, 0))
#         screen.blit(starship.image, starship.rect)
#         mice.draw(screen)
#         lasers.draw(screen)
#
#     if mode == "final_scene":
#         dialogue_mode(alien, final_text)
#
#     pg.display.flip()
#     clock.tick(FPS)



#
# while is_running:
#
# # СОБЫТИЯ
# for event in pg.event.get():
#     if event.type == pg.QUIT:
#         is_running = False
#     if event.type == pg.KEYDOWN:
#         if mo de == "start_scene":
#             text_number += 2
#     if text_number > len(start_text):
#         mode = "meteorites"
#     text_number = 0
#     start_time = time.time()
#     if mode == "alien_scene":
#         text_number += 2
#     if text_number > len(alien_text):
#         mode = "moon"
#     starship.switch_mode()
#     text_number = 0
#     start_time = time.time()
#     if mode == "moon":
#         if event.key == pg.K_SPACE:
#         lasers.add(Laser(starship.rect.midtop))
#         # http://laser_sound.play
#     if mode == "final_scene":
#         text_number += 2
#     if text_number >= len(final_text):
#         mode = "end"
#     text_number = 0
#     start_time = time.time()
#     is_running = False
#
# import time
# from sprite import *
# import pygame as pg
#
# def dialogue_mode(sprite, text):
#     ...
#
#
# pg.init()
# pg.mixer.init()
#
# size = (800, 600)
# screen = pg.display.set_mode(size)
# pg.display.set_caption("Космические коты")
#
# FPS = 120
# clock = pg.time.Clock()
#
# is_running = True
# mode = "start_scene"
#
# meteorites = pg.sprite.Group()
# mice = pg.sprite.Group()
# lasers = pg.sprite.Group()
# space=pg.image.load('space.png').convert()
# space=pg.transform.scale(space,size)
# start_text = ["Мы засекли сигнал с планеты Мур.",
#               "",
#               "Наши друзья, инопланетные коты,",
#               "нуждаются в помощи.",
#               "Космические мыши хотят съесть их луну,",
#               "потому что она похожа на сыр.",
#               "Как долго наш народ страдал от них, ",
#               "теперь и муряне в беде...",
#               "Мы должны помочь им.",
#               "Вылетаем прямо сейчас.",
#               "Спасибо, что починил звездолёт, штурман. ",
#               "Наконец-то функция автопилота работает.",
#               "Поехали!"]
#
# alien_text = ["СПАСИТЕ! МЫ ЕЛЕ ДЕРЖИМСЯ!",
#               "",
#               "Мыши уже начали грызть луну...",
#               "Скоро куски луны будут падать на нас.",
#               "Спасите муриан!", ]
#
# final_text = ["Огромное вам спасибо,",
#               "друзья с планеты Мяу!",
#               "Как вас называть? Мяуанцы? Мяуриане?",
#               "В любом случае, ",
#               "теперь наша планета спасена!",
#               "Мы хотим отблагодарить вас.",
#               "Капитан Василий и его штурман получают",
#               "орден SKYSMART.",
#               "А также несколько бутылок нашей",
#               "лучшей валерьянки.",
#               "",
#               ""]
#
# text_number = 0
# f1=pg.font.Font("FRACTAL.otf",25)
# while is_running:
#
#     # СОБЫТИЯ
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             is_running = False
#
#         if event.type==pg.MOUSEBUTTONDOWN:
#             if mode == 'start_scene':
#                 text_number+=2
#                 if text_number > len(start_text):
#                         text_number=0
#                         mode = 'meteorites'
#                 # if event.button == 1:
#
#
#
#     # ОБНОВЛЕНИЯ
#     if mode == "start_scene":
#         screen.blit(space,(0,0))
#         text1 = f1.render(start_text[text_number],True,pg.Color('White'))
#         screen.blit(text1,(280,450))
#         if text_number < len(start_text)-1:
#             text2 = f1.render(start_text[text_number+1], True, pg.Color('White'))
#             screen.blit(text2, (280, 470))
#             text_number+=2
#     if mode == "meteorites":
#         ...
#
#     if mode == "alien_scene":
#         ...
#
#     if mode == "moon":
#         ...
#
#     if mode == "final_scene":
#         ...
#
#     pg.display.flip()
#     clock.tick(FPS)












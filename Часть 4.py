import os
import sys
import pygame
import requests
from pygame.locals import *
import time

fps = 100
clock = pygame.time.Clock()
coord = input().split(',')
coord = ','.join(coord)

map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn=1.0,1.0&l=map"
s = 0.5
inp = 1.0
map_type = 'map'

response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))


def load_image(name, colorkey=None):
    fullname = os.path.join(r'c:\Users\user\PycharmProjects\Решение задач на API Яндекс.Карт', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def im():
    image_shema = pygame.transform.scale(load_image('btn_shema.png'), (95, 42))
    screen.blit(image_shema, (0, 0))
    image_sputnik = pygame.transform.scale(load_image('btn_sputnik.png'), (95, 42))
    screen.blit(image_sputnik, (96, 0))
    image_gibrid = pygame.transform.scale(load_image('btn_gibrid.png'), (95, 42))
    screen.blit(image_gibrid, (192, 0))
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse[0] <= 95 and mouse[1] <= 42:
                map_type = 'map'
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn={inp},{inp}&l={map_type}"
                os.remove(map_file)
                response = requests.get(map_request)
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            elif (mouse[0] >= 96 and mouse[0] <= 191) and mouse[1] <= 42:
                map_type = 'sat'
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn={inp},{inp}&l={map_type}"
                os.remove(map_file)
                response = requests.get(map_request)
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            elif (mouse[0] >= 192 and mouse[0] <= 287) and mouse[1] <= 42:
                map_type = 'skl'
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn={inp},{inp}&l={map_type}"
                os.remove(map_file)
                response = requests.get(map_request)
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
        if event.type == KEYUP:
            if event.key == K_PAGEUP:
                if inp < 18.0:
                    inp = inp + 0.5
                    map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn={inp},{inp}&l={map_type}"
                    os.remove(map_file)
                    response = requests.get(map_request)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
            if event.key == K_PAGEDOWN:
                if inp > 0.1:
                    inp = inp - 0.5
                    map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn={inp},{inp}&l={map_type}"
                    os.remove(map_file)
                    response = requests.get(map_request)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
        if event.type == KEYDOWN:  # 30.317144736101078,59.93284643499016
            if event.key == K_LEFT:
                if float(coord[0]) >= -180:
                    coord = coord.split(',')
                    coord = str(float(coord[0]) - 0.1), coord[1]
                    coord = ','.join(coord)
                    map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn={inp},{inp}&l={map_type}"
                    os.remove(map_file)
                    response = requests.get(map_request)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
            if event.key == K_RIGHT:
                if float(coord[0]) <= 180:
                    coord = coord.split(',')
                    coord = str(float(coord[0]) + 0.1), coord[1]
                    coord = ','.join(coord)
                    map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn={inp},{inp}&l={map_type}"
                    os.remove(map_file)
                    response = requests.get(map_request)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
            if event.key == K_UP:
                coord = coord.split(',')
                if float(coord[1]) <= 90:
                    coord = coord[0], str(float(coord[1]) + 0.1)
                    coord = ','.join(coord)
                    map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn={inp},{inp}&l={map_type}"
                    os.remove(map_file)
                    response = requests.get(map_request)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
            if event.key == K_DOWN:
                coord = coord.split(',')
                if float(coord[1]) >= -90:
                    coord = coord[0], str(float(coord[1]) - 0.1)
                    coord = ','.join(coord)
                    map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn={inp},{inp}&l={map_type}"
                    os.remove(map_file)
                    response = requests.get(map_request)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    im()
    pygame.display.flip()

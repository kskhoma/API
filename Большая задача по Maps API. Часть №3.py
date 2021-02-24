import os
import sys
import pygame
import requests
from pygame.locals import *

coord = input().split(',')
coord = ','.join(coord)

map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn=1.0,1.0&l=map"
s = 0.5
inp = 1.0

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
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_PAGEUP:
                if inp < 18.0:
                    inp = inp + 0.5
                    map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn={inp},{inp}&l=map"
                    os.remove(map_file)
                    response = requests.get(map_request)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
            if event.key == K_PAGEDOWN:
                if inp > 0.1:
                    inp = inp - 0.5
                    map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn={inp},{inp}&l=map"
                    os.remove(map_file)
                    response = requests.get(map_request)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                coord = coord.split(',')
                coord = float(coord[0]) - 1.0, coord[1]
                coord = ','.join(coord)
                print(coord)
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={coord}&spn={inp},{inp}&l=map"
                os.remove(map_file)
                response = requests.get(map_request)
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
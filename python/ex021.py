"""Cabeçalho 021:
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3."""

import pygame
pygame.init()

#pygame.mixer.music.load('skrillet_fell_invincible.mpeg')
pygame.mixer.music.load('skrillet_the_resistance.mpeg')
#pygame.mixer.music.load('skrillet_monster.mpeg')
pygame.mixer.music.play()
input()
pygame.event.wait()

# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 16:57:40 2021

@author: Antonio Muñoz Santiago
"""

import pygame
import pygame.time as GAME_TIME
import math

import bullet

class Enemy:
    def __init__(self, surface, x0, y0, size):
        
        # Dimensiones del sprite
        self.size = size
        
        # Cargamos y redimensionamos la imagen
        self.image = pygame.image.load("assets/images/enemy.png")
        self.image = pygame.transform.scale(self.image, (size, size))
        
        self.surface = surface
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = x0
        self.rect.centery = y0
        
        # Tiempo entre disparos (en ms)
        self.delay = 1500
        self.lastShot = GAME_TIME.get_ticks()
        
        self.bullets = []
        
    def update(self, dt):
        
        if GAME_TIME.get_ticks()-self.lastShot >= self.delay:
            angle = 0
            while angle <= 360:
                self.bullets.append(bullet.Bullet(self.surface, self.rect.centerx, 
                                              self.rect.centery, 20, 
                                              0.25+abs(0.1*math.sin(6*math.radians(angle))), 
                                              angle))
                angle += 5
            self.lastShot = GAME_TIME.get_ticks()
        
        for each in self.bullets:
            each.update(dt)
            
        # Se eliminan las balas que han salido de la pantalla
        for each in self.bullets:
            if each.isAlive() == False:
                self.bullets.remove(each)
                
        self.surface.blit(self.image, self.rect)
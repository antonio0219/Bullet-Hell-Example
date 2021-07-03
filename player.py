# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:53:28 2021

@author: Antonio Muñoz Santiago

Este archivo contiene:
    - Utilización de la función update, una especie de main loop para cada 
      objeto.
    - Utilización de la función clamp_ip (o clamp) para restringir el movimiento
      de un objeto rect a dentro de otro.
      
Observaciones:
    - Es importante mantener las proporciones en los sprites para que la imagen
      no se deforme al cambiar el tamaño de la pantalla. Esto lo hace la opción
      SCALED.
    - Con la función contains podemos comprobar si un rectángulo está dentro
      de otro.
    - Con pygame.transform podemos realizar ciertas operaciones sobre objetos
      surface.
    - Pygame transforma las coordenadas a enteros, por lo que no hay problema
      en utilizar float.
      
Objetivos:
    - Utilizar las funciones de rect para ver si los objetos colisionan.
"""

import pygame

class Player:
    def __init__(self, surface, x0, y0, size):
        self.VEL = 0.25
        
        self.size = size # Tamaño del sprite
        
        # Cargamos y redimensionamos la imagen
        self.image = pygame.image.load("assets/images/ship.png")
        self.image = pygame.transform.scale(self.image, (size, size))
        
        self.surface = surface
        
        # Creamos el objeto rectángulo asociado a la imagen
        self.rect = self.image.get_rect()
        
        self.rect.centerx = x0
        self.rect.centery = y0
        
    def update(self, held_keys, dt):
        
        # Se multiplica la velocidad por el delta time.
        self.rect.centerx += self.VEL * held_keys[pygame.K_d] * dt
        self.rect.centerx -= self.VEL * held_keys[pygame.K_a] * dt
        self.rect.centery -= self.VEL * held_keys[pygame.K_w] * dt
        self.rect.centery += self.VEL * held_keys[pygame.K_s] * dt
        
        # Restringimos el movimiento del rectángulo a las dimensiones de la
        # pantalla. clamp_ip modifica el rectángulo sobre el que se ejecuta.
        self.rect.clamp_ip(self.surface.get_rect())
        
        self.surface.blit(self.image, self.rect)

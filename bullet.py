# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:59:29 2021

@author: Antonio Muñoz Santiago

El ejemplo contiene:
    - Utilización de un vector velocidad en polares para controlar la 
      trayectoria (posteriormente se pasa a cartesianas).
    - Utilización de la función colliderect(), que devuelve true si los dos
      rectángulos se superponen.
      
Observaciones:
    - math.sin() requiere el argumento en grados.
    - Los ángulos en este caso irían en sentido antihorario (porque el eje y 
      va hacia abajo).
    - Al asignar un float a rect.centerx se almacena como entero, por lo que
      si se elimina la parte decimal en cada frame la trayectoria se verá 
      modificada. Esto se puede solucionar sumando sobre un float y asignando 
      ese float a las coordenadas del objeto rectángulo, para no perder posición.
"""

import pygame
import math

class Bullet:
    def __init__(self, surface, x0, y0, size, module, angle):
        
        # Vector velocidad, en polares (módulo y ángulo, en grados)
        self.VEL = (module, angle)
        
        # Dimensiones del sprite
        self.size = size
        
        # Cargamos y redimensionamos la imagen
        self.image = pygame.image.load("assets/images/bullet.png")
        self.image = pygame.transform.scale(self.image, (size, size))
        
        self.surface = surface
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = x0
        self.rect.centery = y0
        
        # Variables auxiliares para la posición
        self.posx = x0
        self.posy = y0
        
        self.alive = True
    
    def isAlive(self):
        return self.alive
    
    def update(self, dt):
        
        # Actualizamos las posiciones
        
        self.posx += self.VEL[0]*math.cos(math.radians(self.VEL[1]))*dt
        self.posy += self.VEL[0]*math.sin(math.radians(self.VEL[1]))*dt
        
        self.rect.centerx = self.posx
        self.rect.centery = self.posy
        
        # Comprobamos si está dentro de la pantalla
        if not self.rect.colliderect(self.surface.get_rect()):
            self.alive = False
        
        self.surface.blit(self.image, self.rect)
        

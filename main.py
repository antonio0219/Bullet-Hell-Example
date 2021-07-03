# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:16:54 2021

@author: Antonio Muñoz Santiago

El ejemplo contiene:
    - Movimiento de balas en un bullet hell.
    - Utilización de delta-time.
    - Adaptación del juego al tamaño de la pantalla.
    - Utilización de un objeto pygame.key.get_pressed().
    
Observaciones:
    - Para adaptarnos al tamaño de la pantalla se utiliza la opción SCALED al
      llamar a set_mode() (la función que crea la ventana). SCALED se encarga
      de elegir las mejores dimensiones de la pantalla posibles dependiendo
      de la resolución del monitor, aunque el juego siga pensando que tiene
      la resolución con la que trabajemos inicialmente. Funciona tanto con
      RESIZABLE como con FULLSCREEN, manteniendo tanto las proporciones del 
      juego como los eventos de ratón. Se pueden utilizar varias opciones
      conjuntamente con el operador bitwise "|".
    - Con la función get_time() obtenemos el tiempo transcurrido en el frame
      anterior, y con tick(FPS) limitamos los fps y los hacemos estables.
    - Si hiciera falta en otro código sería posible ponerle límites a las
      dimensiones de la pantalla.
"""

import pygame, sys
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import pygame.time as GAME_TIME

import player, enemy

""" CONSTANTES """
# Dimensiones por defecto de la pantalla
WINDOW_WIDTH = 950
WINDOW_HEIGHT = 650

# Fps máximos
FPS = 60

""" VARIABLES """
state = "IN GAME"

pygame.init() # Se inicializan los módulos de pygame

""" OBJETOS """
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),
                                  pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("Bullet Hell Example")
clock = GAME_TIME.Clock()

player = player.Player(surface, surface.get_width()/2,
                       3*surface.get_height()/4, 60)
enemy = enemy.Enemy(surface, surface.get_width()/2, 
                    surface.get_height()/4, 60)

""" FUNCIONES """
def quitGame(): # Para detener la ejecución del juego
    pygame.quit()
    sys.exit()
    
def drawStage(surface):
    surface.fill((255,255,255))

""" MAIN LOOP """
while True:
    drawStage(surface)
    
    held_keys = pygame.key.get_pressed()
    
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            quitGame()
            
    if state == "IN GAME":
        # Pasamos como argumento a player y enemy el delta time.
        # get_time() devuelve en ms el tiempo transcurrido en el frame anterior.
        enemy.update(clock.get_time())
        player.update(held_keys, clock.get_time())
    
    # El objeto clock debe ser actualizado una vez por frame. El argumento
    # opcional nos permite limitar los fps.
    clock.tick(FPS)
    pygame.display.update()
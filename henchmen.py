from constants import *
import pygame
import random as rand
from enemy_entity import Enemy_entity

class Henchmen(Enemy_entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.speed = 2
        self.change_direction_timer = 2 #SECONDS

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((200, 0, 0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)

        # self.direction = self.random_vector2()



    def update(self, solid_objects_group, bullet_group):

        self.reverse_direction_move(solid_objects_group, self.speed)
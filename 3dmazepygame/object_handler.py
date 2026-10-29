import pygame as py
from sprite_object import *
from npc import *
import random



class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list =[]
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc

        # sprite map
        #add_sprite(SpriteObject(game))
        #add_sprite(SpriteObject(game, pos=(10.5,2.5)))
        #add_sprite(SpriteObject(game, pos=(8.5,3.5)))
        #add_sprite(SpriteObject(game, pos=(9.5,6.5)))
        add_sprite(SpriteObject(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(SpriteObject(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(SpriteObject(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(SpriteObject(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(SpriteObject(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(SpriteObject(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(SpriteObject(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(SpriteObject(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(SpriteObject(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(SpriteObject(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(SpriteObject(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(SpriteObject(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        #add_sprite(AnimatedSprite(game))
        #add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        #add_sprite(AnimatedSprite(game, pos=(9.5, 8.5)))
        #add_sprite(AnimatedSprite(game, pos=(4.5, 1.5)))
        #add_sprite(AnimatedSprite(game, pos=(6.5, 6.5)))
        #add_sprite(AnimatedSprite(game, pos=(3.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(AnimatedSprite(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(AnimatedSprite(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(AnimatedSprite(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(AnimatedSprite(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(AnimatedSprite(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(AnimatedSprite(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(AnimatedSprite(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(AnimatedSprite(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))
        add_sprite(AnimatedSprite(game, pos=(random.randrange(20) + 0.5, random.randrange(20) + 0.5)))

        # npc map
        add_npc(NPC(game))
        

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)


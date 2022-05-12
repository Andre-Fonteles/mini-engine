import random
import pygame
import engine

class PlayerCharacter(engine.AnimatedObject):
    def __init__(self, x, y, images, velocity_x = 1, velocity_y = 1):
        super().__init__(x, y, images, velocity_x, velocity_y)

    def update(self, game, time_elapsed):
        super().update(game, time_elapsed)

        moving = False

        if(game.key_pressed("up")):
            self.move_up(False)
            moving = True
        if(game.key_pressed("down")):
            self.move_down(False)
            moving = True
        if(game.key_pressed("left")):
            self.move_left()
            moving = True
        if(game.key_pressed("right")):
            self.move_right()
            moving = True
            
        if(game.key_pressed("space")):
            self.play_animation("dance")

        if(moving):
            self.set_default_animation("walking")
        else:
            self.set_default_animation("still")

class DodgeGame(engine.Game):
    def __init__(self, width, heigth):
        super().__init__(width, heigth)

        char_standing_img = pygame.image.load("boy/character1.png")
        char_walking_img = pygame.image.load("boy/character2.png")
        dance_1_img = pygame.image.load("boy/dance1.png")
        dance_2_img = pygame.image.load("boy/dance2.png")

        self.player1 = PlayerCharacter(0, 0, [char_standing_img], 1/4, 1/4)
        self.player1.add_animation("walking", [char_walking_img, char_standing_img], 3)
        self.player1.add_animation("dance", [dance_1_img, dance_2_img], 1)
        self.add_object(self.player1)

    def update(self, time_elapsed):
        pass

game = DodgeGame(600, 400)
game.start()
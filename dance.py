import pygame
import engine

class WalkDanceGame(engine.Game):
    def __init__(self, width, heigth):
        super().__init__(width, heigth)

        char_standing_img = pygame.image.load("character1.png")
        char_walking_img = pygame.image.load("character2.png")
        dance_1_img = pygame.image.load("dance1.png")
        dance_2_img = pygame.image.load("dance2.png")

        self.player1 = engine.Character(0, 0, [char_standing_img], 1/4, 1/4)
        self.player1.add_animation("walking", [char_walking_img, char_standing_img], 3)

        self.player1.add_animation("dance", [dance_1_img, dance_2_img], 1)

        self.add_object(self.player1)
        self.add_object(engine.Character(0, 0, [dance_1_img, dance_2_img], 1/4, 1/4))

    def update(self, time_elapsed):
        p1 = self.player1

        moving = False

        if(self.key_pressed("up")):
            p1.move_up(False)
            moving = True
        if(self.key_pressed("down")):
            p1.move_down(False)
            moving = True
        if(self.key_pressed("left")):
            p1.move_left()
            moving = True
        if(self.key_pressed("right")):
            p1.move_right()
            moving = True
            
        if(self.key_pressed("space")):
            p1.animate_x_times("dance", 1)


        if(moving):
            p1.set_default_animation("walking")
        else:
            p1.set_default_animation("still")

game = WalkDanceGame(600, 400)
game.start()
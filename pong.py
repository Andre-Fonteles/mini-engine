import random
import pygame
import engine

class PongGame(engine.Game):
    def __init__(self, width, heigth):
        super().__init__(width, heigth)

        bar_img = pygame.image.load("pong/bar.png")
        ball_img = pygame.image.load("pong/ball.png")
        
        self.player_2 = engine.AnimatedObject(0, 0, [bar_img])
        self.player_1 = engine.AnimatedObject(width-bar_img.get_width(), 0, [bar_img])
        
        self.ball = engine.AnimatedObject(width/2, 0, [ball_img], .09, .05)

        self.add_object(self.ball)
        self.add_object(self.player_1)
        self.add_object(self.player_2)
        
    def update(self, time_elapsed):
        p1 = self.player_1
        p2 = self.player_2
        ball = self.ball

        ball.move()

        if(self.key_pressed("a")):
            p2.y -= p2.velocity_y * (time_elapsed/4)
        if(self.key_pressed("z")):
            p2.y += p2.velocity_y * (time_elapsed/4)

        if(self.key_pressed("up")):
            p1.y -= p1.velocity_y * (time_elapsed/4)
        if(self.key_pressed("down")):
            p1.y += p1.velocity_y * (time_elapsed/4)
        
        ball.y += ball.velocity_y * (time_elapsed/4)
        ball.x += ball.velocity_x * (time_elapsed/4)
        
        if(ball.check_object_collision(self.player_1) or ball.check_object_collision(self.player_2)):
            if(ball.velocity_x > 0):
                ball.velocity_x = -(ball.velocity_x + 0.01)
            else:
                ball.velocity_x = -(ball.velocity_x - 0.01)

        if(ball.y < 0 or ball.y > self.height):
            ball.velocity_y = -(ball.velocity_y)

game = PongGame(600, 400)
game.start()
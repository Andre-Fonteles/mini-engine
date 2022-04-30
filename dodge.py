import random
import pygame
import engine

class PlayerCharacter(engine.AnimatedObject):
    def __init__(self, x, y, images, velocity_x = 1, velocity_y = 1):
        super().__init__(x, y, images, velocity_x, velocity_y)

    def dance(self):
        self.play_animation("dance")

class EnemyCharacter(engine.AnimatedObject):
    def __init__(self, x, y, images, velocity_x = 1, velocity_y = 1):
        super().__init__(x, y, images, velocity_x, velocity_y)

class WalkDanceGame(engine.Game):
    def __init__(self, width, heigth):
        super().__init__(width, heigth)

        char_standing_img = pygame.image.load("character1.png")
        char_walking_img = pygame.image.load("character2.png")
        dance_1_img = pygame.image.load("dance1.png")
        dance_2_img = pygame.image.load("dance2.png")

        self.player1 = PlayerCharacter(0, 0, [char_standing_img], 1/4, 1/4)
        self.player1.add_animation("walking", [char_walking_img, char_standing_img], 3)
        self.player1.add_animation("dance", [dance_1_img, dance_2_img], 1)

        self.add_object(self.player1)

        # self.add_object(engine.Text(10, 10, "Hello Noobs"))

        self.enemy_spawn_delay = 1000
        self.time_to_spawn_enemy = self.enemy_spawn_delay
        self.ball_img = pygame.image.load("ball.png")
        self.enemies = []

        self.game_over = False

    def update(self, time_elapsed):
        if(not self.game_over):
            self.update_player(time_elapsed)
            self.update_enemies(time_elapsed)

    def update_player(self, time_elapsed):
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
            p1.dance()

        if(moving):
            p1.set_default_animation("walking")
        else:
            p1.set_default_animation("still")

    def update_enemies(self, time_elapsed):
        self.time_to_spawn_enemy = self.time_to_spawn_enemy - time_elapsed
        if(self.time_to_spawn_enemy <= 0):
            # Spawn a new enemy
            max_velocity = 0.1

            side = random.randint(1, 2)
            if(side == 1): # Top
                x = random.randint(0, self.width)
                y = 0
                velocity_x = random.uniform(-max_velocity, max_velocity)
                velocity_y = random.uniform(0, max_velocity)
            else: # Bottom
                x = random.randint(0, self.width)
                y = self.height
                velocity_x = random.uniform(-max_velocity, max_velocity)
                velocity_y = random.uniform(-max_velocity, 0)

            new_enemy = EnemyCharacter(x, y, [self.ball_img], velocity_x, velocity_y)
            self.enemies.append(new_enemy)
            self.add_object(new_enemy)
            self.time_to_spawn_enemy = self.enemy_spawn_delay

        for enemy in self.enemies:
            enemy.move()
            if(enemy.check_character_collision(self.player1)):
                self.add_object(engine.Text(300, 200, "Game Over!"))
                self.game_over = True


game = WalkDanceGame(600, 400)
game.start()
import random
import pygame
import engine

class PlayerCharacter(engine.AnimatedObject):
    def __init__(self, x, y, images, velocity_x = 1, velocity_y = 1, animation_speed = 1):
        super().__init__(x, y, images, velocity_x, velocity_y, animation_speed)
        self.alive = True

    def die(self):
        self.alive = False
        self.set_default_animation("still")

    def update(self, game, time_elapsed):
        super().update(game, time_elapsed)

        if(self.alive):
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
                
            if(moving):
                self.set_default_animation("walking")
            else:
                self.set_default_animation("still")

class EnemyCharacter(engine.AnimatedObject):
    def __init__(self, x, y, images, velocity_x = 1, velocity_y = 1, animation_speed = 1):
        super().__init__(x, y, images, velocity_x, velocity_y, animation_speed)

    def update(self, game, time_elapsed):
        super().update(game, time_elapsed)
        self.move()


class DodgeGame(engine.Game):
    def __init__(self, width, heigth):
        super().__init__(width, heigth)

        # Configure player
        player_still_img = pygame.image.load("boy/character1.png")
        char_walking_img = pygame.image.load("boy/character2.png")
        self.player_1 = PlayerCharacter(0, 0, [player_still_img], 1/4, 1/4)
        self.player_1.add_animation("walking", [char_walking_img, player_still_img], 3)
        self.add_object(self.player_1)

        # Configure some variables related to spawing enemies
        self.enemies = []
        self.enemy_spawn_delay = 1000 # Enemy spawn every second (1000 milliseconds)
        self.time_to_spawn_enemy = self.enemy_spawn_delay # Countdown for the next enemy
        self.roach_1_img = pygame.image.load("roach/roach1.png")
        self.roach_2_img = pygame.image.load("roach/roach2.png")

        self.game_over = False

        # Configure clock
        self.timer = engine.Timer(10, 10, color=(0, 0, 0))
        self.add_object(self.timer)

    def update(self, time_elapsed):
        if(not self.game_over):
            # Spawn a new roach if it is time
            self.spawn_enemies(time_elapsed)

            # Check if any roach collides with player
            for enemy in self.enemies:
                if(enemy.check_object_collision(self.player_1)):
                    # Game over
                    game_over_text = engine.Text(300, 200, "Game Over!", 36, color=(0, 0, 0))
                    game_over_text.x = self.width/2 - game_over_text.get_width()/2
                    game_over_text.y = self.height/2 - game_over_text.get_height()/2
                    self.add_object(game_over_text)
                    self.game_over = True
                    self.player_1.die()
                    self.timer.pause()


    def spawn_enemies(self, time_elapsed):
        self.time_to_spawn_enemy = self.time_to_spawn_enemy - time_elapsed

        if(self.time_to_spawn_enemy <= 0):
            # Configure attributes of new roach
            max_velocity = 0.1
            side = random.randint(1, 2)
            x = random.randint(0, self.width)
            velocity_x = random.uniform(-max_velocity, max_velocity)
            if(side == 1): # From Top
                y = 0
                velocity_y = random.uniform(0, max_velocity)
            else: # From Bottom
                y = self.height
                velocity_y = random.uniform(-max_velocity, 0)

            # Spawn new roach
            roach_imgs = [self.roach_1_img, self.roach_2_img]
            new_enemy = EnemyCharacter(x, y, roach_imgs, velocity_x, velocity_y, 6)
            self.enemies.append(new_enemy)
            self.add_object(new_enemy, 0)
            self.time_to_spawn_enemy = self.enemy_spawn_delay

game = DodgeGame(600, 400)
game.start()
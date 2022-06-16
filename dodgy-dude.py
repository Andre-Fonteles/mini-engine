import random
import pygame
import engine

class PlayerCharacter(engine.AnimatedObject):
    def __init__(self, x, y, images, velocity_x = 1, velocity_y = 1, animation_speed = 1):
        super().__init__(x, y, images, velocity_x, velocity_y, animation_speed)
        self.alive = True

    def get_rectangle(self):
        # Define the rectangle representing the character. Collisions are tested agasint this rectangle. 
        return (self.x+20, self.y + 20, self.get_surface().get_width() - 40, self.get_surface().get_height() - 40)

    def die(self):
        self.alive = False
        self.play_animation("dying", 1)
        self.set_default_animation("dead")

    def do_special(self):
        self.play_animation("special")

    def update(self, game, time_elapsed):
        super().update(game, time_elapsed)

        if(self.alive):

            if(game.key_pressed("space")):
                self.do_special()
            else:
                moving = False

                # Update player according to key board events
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

        # Load player idle animation images
        idle_anim = []
        for i in range(1, 6):
            img = pygame.transform.scale(pygame.image.load("dude/player-idle-{0}.png".format(i)), (416//4, 454//4))
            idle_anim.append(img)

        # Load player walking animation images
        walking_anim = []
        for i in range(1, 9):
            img = pygame.transform.scale(pygame.image.load("dude/player-run-{0}.png".format(i)), (416//4, 454//4))
            walking_anim.append(img)

        # Load player special animation images
        special_anim =  []
        for i in range(1, 3):
            img = pygame.transform.scale(pygame.image.load("dude/player-special-{0}.png".format(i)), (416//4, 454//4))
            special_anim.append(img)

        # Load player dying animation images
        dying_anim =  []
        for i in range(1, 2):
            img = pygame.transform.scale(pygame.image.load("dude/player-idle-{0}.png".format(i)), (416//4, 454//4))
            dying_anim.append(img)

        # Configure player
        self.player_1 = PlayerCharacter(0, 0, idle_anim, 1/4, 1/4, animation_speed=4)
        self.player_1.add_animation("walking", walking_anim, 9)
        self.player_1.add_animation("dying", dying_anim, 14)
        self.player_1.add_animation("special", special_anim, 10)
        self.player_1.add_animation("dead", [dying_anim[-1]])
        
        self.add_object(self.player_1)

        # Configure some variables related to spawing enemies
        self.enemies = []
        self.enemy_spawn_delay = 1000 # Enemy spawn every second (1000 milliseconds)
        self.time_to_spawn_enemy = self.enemy_spawn_delay # Countdown for the next enemy
        self.enemy1_1_img = pygame.transform.scale(pygame.image.load("dude/enemy1-run-1.png"), (30, 30))
        self.enemy1_2_img = pygame.transform.scale(pygame.image.load("dude/enemy1-run-2.png"), (30, 30))
        self.enemy2_1_img = pygame.transform.scale(pygame.image.load("dude/enemy2-run-1.png"), (50, 50))
        self.enemy2_2_img = pygame.transform.scale(pygame.image.load("dude/enemy2-run-2.png"), (50, 50))

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
            if(random.randint(0, 3) == 0):
                enemy_imgs = [self.enemy2_1_img, self.enemy2_2_img]
            else:
                enemy_imgs = [self.enemy1_1_img, self.enemy1_2_img]

            new_enemy = EnemyCharacter(x, y, enemy_imgs, velocity_x, velocity_y, 6)

            self.enemies.append(new_enemy)
            self.add_object(new_enemy, 0)
            self.time_to_spawn_enemy = self.enemy_spawn_delay

# Entry point of the program. 
# Create a new game and start it.
game = DodgeGame(600, 400)
game.start()
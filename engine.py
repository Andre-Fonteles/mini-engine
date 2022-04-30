import datetime
from enum import Enum
from timeit import repeat
import pygame
import pygame.locals

import pygame

class Game:
    def __init__(self, width, heigth):
        self.__finished = False
        self.__keys_pressed = {}
        self.__init_event_dict()

        self.width = width
        self.height = heigth

        self.__objects = []

        pygame.init()

        flags = pygame.locals.DOUBLEBUF
        self.screen = pygame.display.set_mode((width, heigth), flags, 16)

    def add_object(self, obj, index = None):
        if(index == None):
            self.__objects.append(obj)
        else:
            self.__objects.insert(index, obj)
        

    def remove_object(self, obj):
        self.__objects.remove(obj)

    def get_objects(self):
        return self.__objects

    def close(self):
        self.__finished = True

    def start(self):
        self.__last_update = datetime.datetime.now()
        self.__last_render = datetime.datetime.now()
        self.__run()

    def __run(self):        
        while(not self.__finished):
            self.__read_events()
            
            time_now = datetime.datetime.now()

            if((time_now - self.__last_update).microseconds >= 5000):
                time_lapsed = (time_now - self.__last_update).microseconds/1000
                for obj in self.__objects:
                    obj.update(time_lapsed)
                
                self.update(time_lapsed)
                
                # Render objects
                self.screen.fill((0, 0, 0))
                for obj in self.__objects:
                    self.screen.blit(obj.get_image(), (obj.x, obj.y))

                self.__last_update = time_now
                
            time_now = datetime.datetime.now()
            if((time_now - self.__last_render).microseconds >= 11000):
                pygame.display.flip()
                self.__last_render = time_now
            
    def __read_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
            
            if event.type == pygame.KEYDOWN:
                self.__keys_pressed[event.key] = True
            if event.type == pygame.KEYUP:
                self.__keys_pressed[event.key] = False

    def key_pressed(self, key_str):
        key = self.__key_event[key_str.lower()]
            
        if(key in self.__keys_pressed):
            return self.__keys_pressed[self.__key_event[key_str]]
        else:
            return False

    def update(self, time_elapsed):
        pass

    def __init_event_dict(self):
        self.__key_event = {
            "0" : pygame.K_0,
            "1" : pygame.K_1,
            "2" : pygame.K_2,
            "3" : pygame.K_3,
            "4" : pygame.K_4,
            "5" : pygame.K_5,
            "6" : pygame.K_6,
            "7" : pygame.K_7,
            "8" : pygame.K_8,
            "9" : pygame.K_9,
            #"ac_back" : pygame.K_AC_BACK,
            "&" : pygame.K_AMPERSAND,
            "*" : pygame.K_ASTERISK,
            "at" : pygame.K_AT,
            "@" : pygame.K_AT,
            "backquote" : pygame.K_BACKQUOTE,
            "backslash" : pygame.K_BACKSLASH,
            "backspace" : pygame.K_BACKSPACE,
            "break" : pygame.K_BREAK,
            "capslock" : pygame.K_CAPSLOCK,
            "^" : pygame.K_CARET,
            "clear" : pygame.K_CLEAR,
            ":" : pygame.K_COLON,
            "," : pygame.K_COMMA,
            #"$" : pygame.K_CURRENCYSUBUNIT,
            #"$" : pygame.K_CURRENCYUNIT,
            "delete" : pygame.K_DELETE,
            "$" : pygame.K_DOLLAR,
            "down" : pygame.K_DOWN,
            "end" : pygame.K_END,
            "=" : pygame.K_EQUALS,
            "esc" : pygame.K_ESCAPE,
            "escape" : pygame.K_ESCAPE,
            "€" : pygame.K_EURO,
            "!" : pygame.K_EXCLAIM,
            "F1" : pygame.K_F1,
            "F10" : pygame.K_F10,
            "F11" : pygame.K_F11,
            "F12" : pygame.K_F12,
            "F13" : pygame.K_F13,
            "F14" : pygame.K_F14,
            "F15" : pygame.K_F15,
            "F2" : pygame.K_F2,
            "F3" : pygame.K_F3,
            "F4" : pygame.K_F4,
            "F5" : pygame.K_F5,
            "F6" : pygame.K_F6,
            "F7" : pygame.K_F7,
            "F8" : pygame.K_F8,
            "F9" : pygame.K_F9,
            ">" : pygame.K_GREATER,
            "#" : pygame.K_HASH,
            "help" : pygame.K_HELP,
            "home" : pygame.K_HOME,
            "insert" : pygame.K_INSERT,
            "K_KP0" : pygame.K_KP0,
            "K_KP1" : pygame.K_KP1,
            "K_KP2" : pygame.K_KP2,
            "K_KP3" : pygame.K_KP3,
            "K_KP4" : pygame.K_KP4,
            "K_KP5" : pygame.K_KP5,
            "K_KP6" : pygame.K_KP6,
            "K_KP7" : pygame.K_KP7,
            "K_KP8" : pygame.K_KP8,
            "K_KP9" : pygame.K_KP9,
            "K_KP_0" : pygame.K_KP_0,
            "K_KP_1" : pygame.K_KP_1,
            "K_KP_2" : pygame.K_KP_2,
            "K_KP_3" : pygame.K_KP_3,
            "K_KP_4" : pygame.K_KP_4,
            "K_KP_5" : pygame.K_KP_5,
            "K_KP_6" : pygame.K_KP_6,
            "K_KP_7" : pygame.K_KP_7,
            "K_KP_8" : pygame.K_KP_8,
            "K_KP_9" : pygame.K_KP_9,
            "/" : pygame.K_KP_DIVIDE,
            "enter" : pygame.K_KP_ENTER,
            "=" : pygame.K_KP_EQUALS,
            "-" : pygame.K_KP_MINUS,
            "*" : pygame.K_KP_MULTIPLY,
            "." : pygame.K_KP_PERIOD,
            "+" : pygame.K_KP_PLUS,
            "alt" : pygame.K_LALT,
            "left alt" : pygame.K_LALT,
            "control" : pygame.K_LCTRL,
            "left control" : pygame.K_LCTRL,
            "left" : pygame.K_LEFT,
            "[" : pygame.K_LEFTBRACKET,
            "(" : pygame.K_LEFTPAREN,
            "<" : pygame.K_LESS,
            #"L" : pygame.K_LGUI,
            #"L" : pygame.K_LMETA,
            "shift" : pygame.K_LSHIFT,
            "left shift" : pygame.K_LSHIFT,
            "super" : pygame.K_LSUPER,
            "left super" : pygame.K_LSUPER,
            #"M" : pygame.K_MENU,
            "-" : pygame.K_MINUS,
            #"M" : pygame.K_MODE,
            #"N" : pygame.K_NUMLOCK,
            #"N" : pygame.K_NUMLOCKCLEAR,
            "page down" : pygame.K_PAGEDOWN,
            "page up" : pygame.K_PAGEUP,
            "pause" : pygame.K_PAUSE,
            "%" : pygame.K_PERCENT,
            "." : pygame.K_PERIOD,
            "+" : pygame.K_PLUS,
            #"P" : pygame.K_POWER,
            #"P" : pygame.K_PRINT,
            "printscreen" : pygame.K_PRINTSCREEN,
            "?" : pygame.K_QUESTION,
            "'" : pygame.K_QUOTE,
            "\"" : pygame.K_QUOTEDBL,
            "right alt" : pygame.K_RALT,
            "right control" : pygame.K_RCTRL,
            "return" : pygame.K_RETURN,
            #"R" : pygame.K_RGUI,
            "right" : pygame.K_RIGHT,
            "]" : pygame.K_RIGHTBRACKET,
            ")" : pygame.K_RIGHTPAREN,
            #"R" : pygame.K_RMETA,
            "right shift" : pygame.K_RSHIFT,
            "right super" : pygame.K_RSUPER,
            #"S" : pygame.K_SCROLLLOCK,
            #"S" : pygame.K_SCROLLOCK,
            ";" : pygame.K_SEMICOLON,
            "/" : pygame.K_SLASH,
            "space" : pygame.K_SPACE,
            " " : pygame.K_SPACE,
            #"S" : pygame.K_SYSREQ,
            "tab" : pygame.K_TAB,
            "_" : pygame.K_UNDERSCORE,
            #"U" : pygame.K_UNKNOWN,
            "up" : pygame.K_UP,
            "a" : pygame.K_a,
            "b" : pygame.K_b,
            "c" : pygame.K_c,
            "d" : pygame.K_d,
            "e" : pygame.K_e,
            "f" : pygame.K_f,
            "g" : pygame.K_g,
            "h" : pygame.K_h,
            "i" : pygame.K_i,
            "j" : pygame.K_j,
            "k" : pygame.K_k,
            "l" : pygame.K_l,
            "m" : pygame.K_m,
            "n" : pygame.K_n,
            "o" : pygame.K_o,
            "p" : pygame.K_p,
            "q" : pygame.K_q,
            "r" : pygame.K_r,
            "s" : pygame.K_s,
            "t" : pygame.K_t,
            "u" : pygame.K_u,
            "v" : pygame.K_v,
            "w" : pygame.K_w,
            "x" : pygame.K_x,
            "y" : pygame.K_y,
            "z" : pygame.K_z,
        }

class Object:
    def __init__(self, x, y, images):
        self.x = x
        self.y = y
        
        self.__animations = {"still" : Animation(images, 1)}
        self.set_default_animation("still")
        self.special_anim = None

        self.__time_elapsed = 0
        self.set_hor_direction(Direction.LEFT)
        self.set_ver_direction(Direction.UP)

    def get_width(self):
        return self.get_image().get_width()

    def get_width(self):
        return self.get_image().get_height()

    def set_hor_direction(self, direction):
        self.__hor_direction = direction

    def set_ver_direction(self, direction):
        self.__ver_direction = direction

    def get_image(self):
        flip_h = self.__hor_direction == Direction.RIGHT
        flip_v = self.__ver_direction == Direction.DOWN
        if(self.special_anim != None):
            return self.special_anim.get_image(flip_h, flip_v)
        else:
            return self.__default_anim.get_image(flip_h, flip_v)

    def get_time_elapsed(self):
        return self.__time_elapsed

    def update(self, time_elapsed):
        self.__time_elapsed = time_elapsed
        if(self.special_anim != None):
            self.special_anim.update(time_elapsed)
            if(self.special_anim.is_finished()):
                self.special_anim = None
        else:
            self.__default_anim.update(time_elapsed)

    def add_animation(self, key, images, speed = .5):
        self.__animations[key] = Animation(images, speed)

    def set_default_animation(self, key):
        try:
            if(self.__default_anim != self.__animations[key]):
                self.__default_anim.stop()
        except AttributeError:
            pass
        self.__default_anim = self.__animations[key]
        self.__default_anim.repeat = -1 # Repeat forever

    def play_animation(self, anim_key, times = 1):
        if(self.special_anim == None):
            self.special_anim = self.__animations[anim_key]
            self.special_anim.stop()
            self.special_anim.repeat = times

    def check_character_collision(self, object):
        return self.check_rectangle_collision(object.get_x(), object.get_y(), object.get_width(), object.get_height())

    def check_rectangle_collision(self, x, y, width, height):
        hor = not(self.x > x+width or self.x + self.width < x)
        ver = not(self.y > y+height or self.y + self.height < y)
        return hor and ver


class Character(Object):
    def __init__(self, x, y, images, velocity_x = 1, velocity_y = 1):
        super().__init__(x, y, images)

        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        
    def move_left(self, face_dir = True):
        if(face_dir):
            self.set_hor_direction(Direction.LEFT)
        self.x -= self.velocity_x * self.get_time_elapsed()

    def move_right(self, face_dir = True):
        if(face_dir):
            self.set_hor_direction(Direction.RIGHT)
        self.x += self.velocity_x * self.get_time_elapsed()

    def move_up(self, face_dir = True):
        if(face_dir):
            self.set_ver_direction(Direction.UP)
        self.y -= self.velocity_y * self.get_time_elapsed()

    def move_down(self, face_dir = True):
        if(face_dir):
            self.set_ver_direction(Direction.DOWN)
        self.y += self.velocity_y * self.get_time_elapsed()

class Animation:
    def __init__(self, images, speed, repeat = -1):
        self.__images = images
        self.__current_img_i = 0
        self.__time_to_transition = 500/speed
        self.__time = 0
        self.repeat = repeat
        self.__repeat_iteration = 0
        self.__finished = False

    def update(self, time_elapsed):
        if(not self.__finished):
            self.__time += time_elapsed
            if(self.__time >= self.__time_to_transition):
                self.__time = 0
                self.__current_img_i = (self.__current_img_i + 1) % len(self.__images)
                
                if(self.repeat != -1 and self.__current_img_i == 0):
                    self.__repeat_iteration += 1
                    if(self.__repeat_iteration >= self.repeat):
                        self.__finished = True
            
    def is_finished(self):
        return self.__finished

    def get_image(self, flip_x, flip_y):
        return pygame.transform.flip(self.__images[self.__current_img_i], flip_x, flip_y)

    def stop(self):
        self.__time = 0
        self.__repeat_iteration = 0
        self.__current_img_i = 0
        self.__finished = False


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
import random
import arcade

WIDTH = 600
HEIGHT = 500
SIZE = 4

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.width = SIZE
        self.height = SIZE
        self.color_1 = arcade.color.BLACK
        self.color_2 = arcade.color.WHITE
        self.body_size = 0
        self.body = []
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        self.speed = 4
        self.change_x = 0
        self.change_y = 0
        self.score = 0

    def eat_apple(self):
        self.body_size += 1
        self.score += 1

    def eat_bahbah(self):
        #self.body_size += 2
        self.score += 2

    def eat_ahah(self):
        #self.body_size -= 1
        self.score -= 1

    def draw(self):
        #arcade.draw_rectangle_outline(self.center_x,self.center_y,self.width,self.height,self.color_1)
        arcade.draw_rectangle_outline(self.center_x,self.center_y,self.width,self.height,arcade.color.BLUE)

        for i , p in enumerate(self.body):
            if i%2 == 0:
                arcade.draw_rectangle_filled(p[0],p[1],self.width,self.height,self.color_1)
            else:
                arcade.draw_rectangle_filled(p[0],p[1],self.width,self.height,self.color_2)

    def move(self):
        self.body.append([self.center_x,self.center_y])

        if len(self.body) > self.body_size:
            self.body.pop(0)


        if self.change_x == -1:
            self.center_x -= self.speed
        elif self.change_x == 1:
            self.center_x += self.speed
        # else:
        #     self.center_x += 0

        if self.change_y == -1:
            self.center_y -= self.speed
        elif self.change_y == 1:
            self.center_y += self.speed


        # if self.center_x < 0:
        #     self.center_x = WIDTH
            
        # elif self.center_x > WIDTH+1:
        #     self.center_x = 0

        # if self.center_y < 0:
        #     self.center_y = HEIGHT
        # elif self.center_y > HEIGHT+1:
        #     self.center_y = 0
        

class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        
        self.width = SIZE*3
        self.height = SIZE*3
        self.color = arcade.color.RED
        self.r = 10
        self.center_x = random.randint(0,WIDTH-100)
        self.center_y = random.randint(0,HEIGHT-100)
        
    def draw(self):
        arcade.draw_circle_outline(self.center_x,self.center_y,self.r,self.color)

class Bahbah(arcade.Sprite):
    def __init__(self):
        super().__init__()
        
        self.width = SIZE*2
        self.height = SIZE*2
        self.color = arcade.color.YELLOW
        self.r = 4
        self.center_x = random.randint(0,WIDTH-50)
        self.center_y = random.randint(0,HEIGHT-50)
        
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

class Ahah(arcade.Sprite):
    def __init__(self):
        super().__init__()
        
        self.width = SIZE*4
        self.height = SIZE*4
        self.color = arcade.color.BROWN
        self.r = 6
        self.center_x = random.randint(0,WIDTH-10)
        self.center_y = random.randint(0,HEIGHT-10)
        
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=WIDTH,height=HEIGHT,title="snake",resizable=True)
        arcade.set_background_color(arcade.color.GREEN)
        
        self.snake = Snake()
        self.apple = Apple()
        self.bahbah = Bahbah()
        self.ahah = Ahah()

    def on_draw(self):
        arcade.start_render()

        if (self.snake.center_x < 0) or (self.snake.center_x > WIDTH) or (self.snake.center_y < 0) or (self.snake.center_y > HEIGHT):
            self.snake.score = -1
            # out = f"score: {self.snake.score}"
            # arcade.draw_text(out,5,5,arcade.color.BLACK,15)


        if self.snake.score >=0:
        #arcade.draw_text("Game!!!",5,5,arcade.color.BLACK,15)
            out = f"score: {self.snake.score}"
            arcade.draw_text(out,5,5,arcade.color.BLACK,15)

            self.snake.draw()
            self.apple.draw()
            self.bahbah.draw()
            self.ahah.draw()
        else:
            arcade.draw_text("over",0,250,arcade.color.BLACK,width=600,font_size=15,align='center')

        

    def on_update(self, delta_time: float):
        self.snake.move()

        if arcade.check_for_collision(self.snake,self.apple):
            self.snake.eat_apple()
            self.apple = Apple()

        elif arcade.check_for_collision(self.snake,self.bahbah):
            self.snake.eat_bahbah()
            self.bahbah = Bahbah()

        elif arcade.check_for_collision(self.snake,self.ahah):
            self.snake.eat_ahah()
            self.ahah = Ahah()

#    def on_key_press(self, key: int, modifiers: int):  
    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            #self.snake.center_x -= self.snake.speed
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT:
            #self.snake.center_x += self.snake.speed
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.UP:
            #self.snake.center_y += self.snake.speed
            self.snake.change_y = 1
            self.snake.change_x = 0
        elif key == arcade.key.DOWN:
            #self.snake.center_y -= self.snake.speed
            self.snake.change_y = -1
            self.snake.change_x = 0
        #print(key)
    
my_game = Game()
arcade.run()

#pgzero
import random
CELL = 50
size_w = 15
size_h = 10
WIDTH = CELL * size_w    #НАЖМИ НА ПРОБЕЛ В МЕНЮ
HEIGHT = CELL * size_h
TITLE = "🐍Змея🐍"
FPS = 30
menu_menu = Actor("menu")
play_button = Actor("play_button", (375, 250))
kube1 = Actor("kube1")
kube2 = Actor("kube2")
snake = Actor("zmeyka_golova3", (75, 75))
apple = Actor("apple")
end = 0
menu = 1
count = 0
direction = "RIGHT"
speed = 0.8

snake_map = [  [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2 ,1],
               [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1 ,2],
               [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2 ,1],
               [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1 ,2],
               [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2 ,1],
               [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1 ,2],
               [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2 ,1],
               [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1 ,2],
               [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2 ,1],
               [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1 ,2]  ]
def map_draw():
    for i in range(len(snake_map)):
        for j in range(len(snake_map[0])):
            if snake_map[i][j] == 1:
                kube1.left = CELL*j
                kube1.top = CELL*i
                kube1.draw()
            elif snake_map[i][j] == 2:
                kube2.left = CELL*j
                kube2.top = CELL*i
                kube2.draw()



def start_game():
    global menu, end, direction
    menu = 0
    end = 0
    count = 0
    direction = "RIGHT"
    snake.x = 75
    snake.y = 75
    new_apple()
    schedule_interval(move_snake, speed)
    




def on_mouse_down(button, pos):
    global menu
    if menu == 1 and button == mouse.LEFT and play_button.collidepoint(pos):
        start_game()
            


def draw():
    global end, menu, count
    screen.clear()
    if menu == 1:
        menu_menu.draw()
        play_button.draw()
        screen.draw.text("ЗМЕЙКА", center=(375, 100), fontsize=35, color="blue")
        if keyboard.space:
            photo.draw()
    else:
        map_draw()
        snake.draw()
        apple.draw()
        screen.draw.text(count, center=(20, 20), fontsize=30, color="blue")
        

        
    if snake.x < 0 or snake.x > WIDTH or snake.y < 0 or snake.y > HEIGHT:
        end = 1
    
    if end == 1:
        screen.draw.text("Яблок съеденно:", center=(370, 200), fontsize=30, color="blue")
        screen.draw.text(count, center=(370, 250), fontsize=30, color="blue")
        screen.draw.text("!GAME OVER!", center=(370, 290), fontsize=30, color="red")
        screen.draw.text("НАЖМИТЕ ENTER ЧТОБЫ ПЕРЕЙТИ В МЕНЮ", center=(370, 330), fontsize=30, color="red")
    

def new_apple():
    apple.x = random.randint(0, size_w - 1) * CELL + CELL // 2
    apple.y = random.randint(0, size_h - 1) * CELL + CELL // 2

        
    
def move_snake():
    global count 
    if end == 0:
        if direction == "UP":
            snake.y -= CELL
        elif direction == "DOWN":
            snake.y += CELL
        elif direction == "LEFT":
            snake.x -= CELL
        elif direction == "RIGHT":
            snake.x += CELL
        
        if snake.colliderect(apple):
            new_apple()
            count += 1


def on_key_down(key):
    global direction, end, menu, count
    if end == 0:
        if keyboard.w:
            direction = "UP"
            snake.image = "zmeyka_golova4"
        elif keyboard.s:
            direction = "DOWN"
            snake.image = "zmeyka_golova1"
        elif keyboard.a:
            direction = "LEFT"
            snake.image = "zmeyka_golova2"
        elif keyboard.d:
            direction = "RIGHT"
            snake.image = "zmeyka_golova3"           
    else:
        if keyboard.enter:
            snake.x = 75
            snake.y = 75
            direction = "RIGHT"
            end = 0
            menu = 1
            count = 0

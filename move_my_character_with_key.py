from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character_idle = load_image('Pinkbean_Idle.png')
character_move = load_image('Pinkbean_Move.png')

running = True
x, y, diff = 0, 0, 0
def Move_Left():
    global x
    x = x - diff
def Move_Right():
    global x
    x = x + diff
def Move_Up():
    global y
    y = y + diff

def Move_Down():
    global y
    y = y - diff

def Idle():
    pass
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                Move_Left()
            elif event.key == SDLK_RIGHT:
                Move_Right()
            elif event.key == SDLK_UP:
                Move_Up()
            elif event.key == SDLK_DOWN:
                Move_Down
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                Idle()
            elif event.key == SDLK_RIGHT:
                Idle()
            elif event.key == SDLK_UP:
                Idle()
            elif event.key == SDLK_DOWN:
                Idle()




while running:
    handle_events()
    pass


close_canvas()
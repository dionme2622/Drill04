from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character_idle = load_image('Pinkbean_Idle.png')
character_move = load_image('Pinkbean_Move.png')

direction = 'RIGHT'
running = True
frame, x, y, diff = 0, 0, 0, 0
a, b, c = 0, 0, 0
def Move_Left():
    global x, frame, a, b, c
    x = x - diff
    if frame < 3:
        character_move.clip_composite_draw(0 + a * 102, 0, 113, 126, 0, 'h', 640, 512, 100, 100)
        a = (a + 1) % 3
    elif frame < 5:
        character_move.clip_composite_draw(306 + b * 124, 0, 113, 126, 0, 'h', 640, 512, 100, 100)
        b = (b + 1) % 2
    elif frame < 9:
        character_move.clip_composite_draw(554 + c * 110, 0, 113, 126, 0, 'h', 640, 512, 100, 100)
        c = (c + 1) % 4
    frame = (frame + 1) % 9
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
    global running, direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                Move_Left()
                direction = 'LEFT'
            elif event.key == SDLK_RIGHT:
                Move_Right()
                direction = 'RIGHT'
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
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    handle_events()
    pass


close_canvas()
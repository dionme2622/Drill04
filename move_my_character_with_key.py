from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Jelda.png')

state = 'IDLE_DOWN'
frame = 0
running = True
x, y = 0, 0
num = 7
def handle_events():
    global running
    global x, y
    global state
    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                state = 'LEFT'
            elif event.key == SDLK_RIGHT:
                state = 'RIGHT'
            elif event.key == SDLK_DOWN:
                state = 'DOWN'
            elif event.key == SDLK_UP:
                state = 'UP'
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                state = 'IDLE_LEFT'
            elif event.key == SDLK_RIGHT:
                state = 'IDLE_RIGHT'
            elif event.key == SDLK_DOWN:
                state = 'IDLE_DOWN'
            elif event.key == SDLK_UP:
                state = 'IDLE_UP'
def Character_Left():
    global frame, x, y, num
    x = x - 15
    num = 2
    frame = (frame + 1) % 10
    delay(0.1)
def Character_Right():
    global frame, x, y, num
    x = x + 15
    num = 0
    frame = (frame + 1) % 10
    delay(0.1)

def Character_Up():
    global frame, x, y, num
    y = y + 15
    num = 1
    frame = (frame + 1) % 10
    delay(0.1)

def Character_Down():
    global frame, x, y, num
    y = y - 15
    num = 3
    frame = (frame + 1) % 10
    delay(0.1)

def Character_Left_Idle():
    global frame, x, y, num
    frame = 0
    num = 6
    delay(0.1)
def Character_Right_Idle():
    global frame, x, y, num
    frame = 0
    num = 4
    delay(0.5)
def Character_Up_Idle():
    global frame, x, y, num
    frame = 0
    num = 5
    delay(0.1)
def Character_Down_Idle():
    global frame, x, y, num
    frame = (frame + 1) % 3
    num = 7
    delay(0.1)

while running:
    if state == 'IDLE':
        Character_Up_Idle()
    elif state == 'LEFT':
        Character_Left()
    elif state == 'RIGHT':
        Character_Right()
    elif state == 'UP':
        Character_Up()
    elif state == 'DOWN':
        Character_Down()
    elif state == 'IDLE_LEFT':
        Character_Left_Idle()
    elif state == 'IDLE_RIGHT':
        Character_Right_Idle()
    elif state == 'IDLE_DOWN':
        Character_Down_Idle()
    elif state == 'IDLE_UP':
        Character_Up_Idle()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 120, num * 130, 120, 130, 640 + x, 512 + y)
    update_canvas()
    handle_events()

close_canvas()
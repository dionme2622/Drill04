from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Jelda.png')

state = 'LEFT'
frame = 0
running = True
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
        else:
            state = 'LEFT'
def Character_Idle():
    global frame
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 90, 683, 90, 97, 640, 512)
    update_canvas()
    handle_events()
    frame = (frame+1) % 3
    delay(0.1)
def Character_Left():
    global frame
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 90, 0, 90, 97, 640, 512)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 10
    delay(0.1)
def Character_Right():
    pass

def Character_Up():
    pass

def Character_Down():
    pass



while running:
    if state == 'IDLE':
        Character_Idle()
    elif state == 'LEFT':
        Character_Left()
    elif state == 'RIGHT':
        Character_Right()
    elif state == 'UP':
        Character_Up()
    elif state == 'DOWN':
        Character_Down()


close_canvas()
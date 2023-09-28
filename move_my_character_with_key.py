from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character_idle = load_image('Pinkbean_Idle.png')
character_move = load_image('Pinkbean_Move.png')

running = True

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                pass
            elif event.key == SDLK_RIGHT:
                pass
            elif event.key == SDLK_UP:
                pass
            elif event.key == SDLK_DOWN:
                pass
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                pass
            elif event.key == SDLK_RIGHT:
                pass
            elif event.key == SDLK_UP:
                pass
            elif event.key == SDLK_DOWN:
                pass

while running:
    handle_events()
    pass


close_canvas()
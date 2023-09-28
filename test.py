from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
cm = load_image('Pinkbean_Move.png')
ci = load_image('Pinkbean_Idle.png')


frame = 0
running = True
while running :
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    cm.clip_draw(frame * 100, 0, 113, 126, 640, 512)
    frame = (frame + 1) % 3
    update_canvas()
    delay(0.1)
close_canvas()

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character_idle = load_image('Pinkbean_Idle.png')
character_move = load_image('Pinkbean_Move.png')

move = 'IDLE'
direction = 'RIGHT'
running = True
frame, x, y, diff = 0, 0, 0, 15
a, b, c = 0, 0, 0
dir = 0
def Move_Left():
    global x, frame, a, b, c
    x += dir * diff
    if frame < 3:
        character_move.clip_draw(0 + a * 102, 0, 113, 126, TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y, 100, 100)
        a = (a + 1) % 3
    elif frame < 5:
        character_move.clip_draw(306 + b * 124, 0, 113, 126, TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y, 100, 100)
        b = (b + 1) % 2
    elif frame < 9:
        character_move.clip_draw(554 + c * 110, 0, 113, 126, TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y, 100, 100)
        c = (c + 1) % 4
    frame = (frame + 1) % 9
def Move_Right():
    global x, frame, a, b, c
    x += dir * diff
    if frame < 3:
        character_move.clip_composite_draw(0 + a * 102, 0, 113, 126, 0, 'h', TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y, 100, 100)
        a = (a + 1) % 3
    elif frame < 5:
        character_move.clip_composite_draw(306 + b * 124, 0, 113, 126, 0, 'h', TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y, 100, 100)
        b = (b + 1) % 2
    elif frame < 9:
        character_move.clip_composite_draw(554 + c * 110, 0, 113, 126, 0, 'h', TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y, 100, 100)
        c = (c + 1) % 4
    frame = (frame + 1) % 9
def Move_Up():
    global y, frame, a, b, c
    y += dir * diff
    if direction == 'LEFT':
        if frame < 3:
            character_move.clip_draw(0 + a * 102, 0, 113, 126, TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y, 100, 100)
            a = (a + 1) % 3
        elif frame < 5:
            character_move.clip_draw(306 + b * 124, 0, 113, 126, TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y, 100, 100)
            b = (b + 1) % 2
        elif frame < 9:
            character_move.clip_draw(554 + c * 110, 0, 113, 126, TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y, 100, 100)
            c = (c + 1) % 4
    elif direction == 'RIGHT':
        if frame < 3:
            character_move.clip_composite_draw(0 + a * 102, 0, 113, 126, 0, 'h', TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y,
                                               100, 100)
            a = (a + 1) % 3
        elif frame < 5:
            character_move.clip_composite_draw(306 + b * 124, 0, 113, 126, 0, 'h', TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y,
                                               100, 100)
            b = (b + 1) % 2
        elif frame < 9:
            character_move.clip_composite_draw(554 + c * 110, 0, 113, 126, 0, 'h', TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y,
                                               100, 100)
            c = (c + 1) % 4
    frame = (frame + 1) % 9
def Move_Down():
    global y, frame, a, b, c
    y += dir * diff
    if direction == 'LEFT':
        if frame < 3:
            character_move.clip_draw(0 + a * 102, 0, 113, 126, TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y, 100, 100)
            a = (a + 1) % 3
        elif frame < 5:
            character_move.clip_draw(306 + b * 124, 0, 113, 126, TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y, 100, 100)
            b = (b + 1) % 2
        elif frame < 9:
            character_move.clip_draw(554 + c * 110, 0, 113, 126, TUK_WIDTH // 2 + x, TUK_HEIGHT // 2 + y, 100, 100)
            c = (c + 1) % 4
    elif direction == 'RIGHT':
        if frame < 3:
            character_move.clip_composite_draw(0 + a * 102, 0, 113, 126, 0, 'h', TUK_WIDTH // 2 + x,
                                               TUK_HEIGHT // 2 + y,
                                               100, 100)
            a = (a + 1) % 3
        elif frame < 5:
            character_move.clip_composite_draw(306 + b * 124, 0, 113, 126, 0, 'h', TUK_WIDTH // 2 + x,
                                               TUK_HEIGHT // 2 + y,
                                               100, 100)
            b = (b + 1) % 2
        elif frame < 9:
            character_move.clip_composite_draw(554 + c * 110, 0, 113, 126, 0, 'h', TUK_WIDTH // 2 + x,
                                               TUK_HEIGHT // 2 + y,
                                               100, 100)
            c = (c + 1) % 4
    frame = (frame + 1) % 9

def Idle():

    pass
def handle_events():
    global running, direction, dir, move
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                dir -= 1
                direction = 'LEFT'
                move = 'LEFT'
            elif event.key == SDLK_RIGHT:
                dir += 1
                direction = 'RIGHT'
                move = 'RIGHT'
            elif event.key == SDLK_UP:
                dir += 1
                move = 'UP'
            elif event.key == SDLK_DOWN:
                dir -= 1
                move = 'DOWN'
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                Idle()
                dir += 1
            elif event.key == SDLK_RIGHT:
                Idle()
                dir -= 1
            elif event.key == SDLK_UP:
                Idle()
                dir -= 1
            elif event.key == SDLK_DOWN:
                Idle()
                dir += 1


while running:
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    # Move_Right()
    if move == 'LEFT':
        Move_Left()
    elif move == 'RIGHT':
        Move_Right()
    elif move == 'UP':
        Move_Up()
    elif move == 'DOWN':
        Move_Down()
    update_canvas()
    handle_events()
    delay(0.1)


close_canvas()
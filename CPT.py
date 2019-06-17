import arcade
import random

WIDTH = 1365
HEIGHT = 710

current_screen = "menu"

x = 0
y = 0
score = 0

# Wall

wall_x = 0
wall_y = 1
wall_width = 2
wall_height = 3
wall_color = 4

wall_1 = [690, 0, 25, random.randrange(0, HEIGHT - 200), arcade.color.RED_DEVIL]
wall_2 = [1390, 0, 25, random.randrange(0, HEIGHT - 200), arcade.color.RED_DEVIL]
bottom_walls = [wall_1, wall_2]

wall_a_x = 0
wall_a_y = 1
wall_a_width = 2
wall_a_height = 3
wall_a_color = 4

wall_a_1 = [690, wall_1[wall_height] + 200, 25, HEIGHT - wall_1[wall_height], arcade.color.RED_DEVIL]
wall_a_2 = [1390, wall_2[wall_height] + 200, 25, HEIGHT - wall_2[wall_height], arcade.color.RED_DEVIL]
top_walls = [wall_a_1, wall_a_2]
up_pressed = False
down_pressed = False

# Hit box

hb_x = 0
hb_y = 1
hb_width = 2
hb_height = 3

hitbox1 = [x + 200, y + 295, 100, 5]
hitbox2 = [x + 100, y + 340, 100, 25]
hitbox3 = [x + 75, y + 395, 250, 10]
all_hb = [hitbox1, hitbox2, hitbox3]

def update(delta_time):
    global up_pressed, down_pressed, x, y, current_screen, top_walls, bottom_walls, score, all_hb
    if current_screen == "play":
        if y <= 290:
            if up_pressed:
                y += 10
                for hitbox in all_hb:
                    hitbox[hb_y] += 10
        if y >= -280:
            if down_pressed:
                y -= 10
                for hitbox in all_hb:
                    hitbox[hb_y] -= 10
        for wallb in bottom_walls:
            wallb[wall_x] -= 10
            if wallb[wall_x] <= -25:
                wallb[wall_x] = 1390
                wallb[wall_height] = random.randrange(0, HEIGHT - 200)
        for wall_a in top_walls:
            wall_a[wall_a_x] -= 10
            if wall_a_1[wall_a_x] <= -25:
                wall_a_1[wall_a_x] = 1390
                wall_a_1[wall_a_y] = wall_1[wall_height] + 200
                wall_a_1[wall_a_height] = HEIGHT - wall_1[wall_height]
            if wall_a_2[wall_a_x] <= -25:
                wall_a_2[wall_a_x] = 1390
                wall_a_2[wall_a_y] = wall_2[wall_height] + 200
                wall_a_2[wall_a_height] = HEIGHT - wall_2[wall_height]
        if score_system(wallb, wall_a) == True:
            score += 1
        if hit_detection() == True:
            current_screen = "score"
    if current_screen == "reset":
        x = 0
        y = 0
        wall_1[wall_x] = 690
        wall_2[wall_x] = 1390
        wall_a_1[wall_a_x] = 690
        wall_a_2[wall_a_x] = 1390
        hitbox1[hb_x] = x + 200
        hitbox1[hb_y] = y + 295
        hitbox2[hb_x] = x + 100
        hitbox2[hb_y] = y + 340
        hitbox3[hb_x] = x + 75
        hitbox3[hb_y] = y + 395
        score = 0
        current_screen = "play"

def score_system(wallb, wall_a):
    for wallb in bottom_walls:
        for wall_a in top_walls:
            if (hitbox1[hb_x] == wallb[wall_x] and hitbox1[hb_y] > wallb[wall_y]
                    + wallb[wall_height] and hitbox1[hb_y] < wall_a[wall_a_y]):
                return True
    else:
        return False

def on_draw():
    global x, y, wall1, score, hitbox1
    arcade.start_render()
    # Draw in here...
    if current_screen == "menu":
        arcade.draw_text("FLY", HEIGHT / 2 - 100, WIDTH / 4, arcade.color.BLACK, font_size=60,
                         font_name="lato")
        arcade.draw_text("Press space to play", HEIGHT / 2 - 100, WIDTH / 4.5, arcade.color.BLACK,
                         font_name="lato")
        arcade.draw_text("Press I to read instructions", HEIGHT / 2 - 100, WIDTH / 5, arcade.color.BLACK,
                         font_name="lato")
    if current_screen == "play":
        draw_helicopter(x, y)
        for wallb in bottom_walls:
            draw_wallb(wallb)
        for wall_a in top_walls:
            draw_wall_a(wall_a)
        arcade.draw_text(f"{score}", 20, 690, arcade.color.BLACK)
    if current_screen == "Instruction":
        arcade.draw_text("What's up! To the helicopter use W to go up and S to go down.",
                         HEIGHT / 2, WIDTH / 2 - 40, arcade.color.BLACK)
        arcade.draw_text("You can use the esc key to leave the game at any time", HEIGHT / 2, WIDTH / 2 - 60,
                         arcade.color.BLACK)
        arcade.draw_text("Press ESC for main menu", HEIGHT / 10, WIDTH / 2 - 40, arcade.color.BLACK)
        arcade.draw_text("ESC = Escape To Menu", HEIGHT / 10, WIDTH / 3, arcade.color.BLACK)
        arcade.draw_text("W = Up:", HEIGHT / 10, WIDTH / 3 - 30, arcade.color.BLACK)
        arcade.draw_text("S = DOWN:", HEIGHT / 10, WIDTH / 3 - 60, arcade.color.BLACK)
        arcade.draw_text("SPACE = START:", HEIGHT / 10, WIDTH / 3 - 90, arcade.color.BLACK)
    if current_screen == "score":
        arcade.draw_text(f"Score: {score}", HEIGHT / 10, WIDTH / 2 - 20, arcade.color.BLACK)
        arcade.draw_text("To return to menu, press ESC", HEIGHT / 10, WIDTH / 2 - 60, arcade.color.BLACK)
        arcade.draw_text("To restart, press SPACE", HEIGHT / 10, WIDTH / 2 - 100, arcade.color.BLACK)

def on_key_press(key, modifiers):
    global up_pressed, down_pressed, current_screen
    if current_screen == "menu":
        if key == arcade.key.SPACE:
            current_screen = "reset"
        if key == arcade.key.I:
            current_screen = "Instruction"
    if current_screen == "Instruction":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
    if current_screen == "play":
        if key == arcade.key.W:
            up_pressed = True
        if key == arcade.key.S:
            down_pressed = True
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
    if current_screen == "score":
        if key == arcade.key.SPACE:
            current_screen = "reset"
        if key == arcade.key.ESCAPE:
            current_screen = "menu"

def on_mouse_press(x, y, button, modifiers):
    pass

def on_key_release(key, modifiers):
    global up_pressed
    if key == arcade.key.W:
        up_pressed = False
    global down_pressed
    if key == arcade.key.S:
        down_pressed = False




# HELICOPTER SHAPES

def draw_helicopter(x, y):
    arcade.draw_xywh_rectangle_filled(x + 200, y + 380, 100, -70, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x + 250, y + 380, 50, -35, arcade.color.WHITE)
    arcade.draw_xywh_rectangle_filled(x + 200, y + 365, -100, -25, arcade.color.BLACK)
    arcade.draw_triangle_filled(x + 200, y + 380, x + 235, y + 380, x + 200, y + 400, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 200, y + 400, 10, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x + 205, y + 405, 120, -10, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x + 195, y + 405, -120, -10, arcade.color.BLACK)
    arcade.draw_triangle_filled(x + 100, y + 365, x + 110, y + 365, x + 100, y + 375, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 100, y + 375, 5, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x + 102.5, y + 377.5, 25, -5, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x + 97.5, y + 377.5, -25, -5, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x + 225, y + 310, 5, -10, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x + 275, y + 310, -5, -10, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x + 200, y + 300, 100, -5, arcade.color.BLACK)

# BOTTOM WALL CODE

def draw_wallb(wallb):
    arcade.draw_xywh_rectangle_filled(wallb[wall_x],
                                      wallb[wall_y],
                                      wallb[wall_width],
                                      wallb[wall_height],
                                      wallb[wall_color])

# TOP WALL CODE

def draw_wall_a(wall_a):
    arcade.draw_xywh_rectangle_filled(wall_a[wall_a_x],
                                      wall_a[wall_a_y],
                                      wall_a[wall_a_width],
                                      wall_a[wall_a_height],
                                      wall_a[wall_a_color])


    # BOTTOM WALL HIT DETECTION

def hit_detection():
    for wall_a in top_walls:
        for wallb in bottom_walls:
            for hitbox in all_hb:
                if (hitbox[hb_y] <= wallb[wall_height] and hitbox[hb_x] < wallb[wall_x] and hitbox[hb_x]
                        + hitbox[hb_width] > wallb[wall_x] + wallb[wall_width] or hitbox[hb_x] +
                        hitbox[hb_width] >= wallb[wall_x] and hitbox[hb_x] + hitbox[hb_width]
                        <= wallb[wall_x] + wallb[wall_width] and hitbox[hb_y] < wallb[wall_height]):
                    return True
                elif (hitbox3[hb_y] >= wall_a[wall_a_y] and hitbox3[hb_x] < wall_a[wall_a_x] and hitbox3[hb_x]
                        + hitbox3[hb_width] > wall_a[wall_a_x] + wall_a[wall_a_width] or hitbox3[hb_x] +
                        hitbox3[hb_width] >= wall_a[wall_a_x] and hitbox3[hb_x] + hitbox3[hb_width]
                        <= wall_a[wall_a_x] + wall_a[wall_a_width] and hitbox3[hb_y] > wall_a[wall_a_y]):
                    return True
    else:
        return False

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()
if __name__ == '__main__':
    setup()
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

green1 = (118, 171, 52)
green2 = (154, 189, 54)
# define your draw functions


def draw_sky():
    global red
    global sky
    sky = (100, 100, red)

    arcade.draw_rectangle_filled(400, 300, 800, 600, sky)

    red += 1


red = 1


def draw_cloud(x, y, z):
    arcade.draw_ellipse_filled(x, y, z*100, z*80, arcade.color.WHITE)
    arcade.draw_ellipse_filled(x + z*100, y - z*30, z*60, z*50, arcade.color.WHITE)
    arcade.draw_ellipse_filled(x - z*100, y - z*30, z*60, z*50, arcade.color.WHITE)


def draw_tree(x, y, z):
    arcade.draw_rectangle_filled(x, y - z*20, z*7, z*15, arcade.color.DONKEY_BROWN)
    arcade.draw_ellipse_filled(x + z*7, y + z*3, z*10, z*10, arcade.color.FOREST_GREEN)
    arcade.draw_ellipse_filled(x, y + z*6, z*10, z*15, arcade.color.FOREST_GREEN)
    arcade.draw_ellipse_filled(x - z*7, y + z*3, z*10, z*10, arcade.color.FOREST_GREEN)
    arcade.draw_ellipse_filled(x + z*5, y - z*8, z*8, z*8, arcade.color.FOREST_GREEN)
    arcade.draw_ellipse_filled(x - z*5, y - z*8, z*8, z*8, arcade.color.FOREST_GREEN)


def draw_rolling_hills():
    arcade.draw_ellipse_filled(450, 150, 150, 100, green2)
    arcade.draw_ellipse_filled(-100, -110, 700, 400, arcade.color.APPLE_GREEN)
    arcade.draw_ellipse_filled(700, -110, 400, 350, green1)


def draw():

    arcade.start_render()

    draw_sky()

    draw_cloud(500, 400, 0.8)
    draw_cloud(650, 500, 0.5)
    draw_cloud(200, 450, 1)

    draw_rolling_hills()

    draw_tree(50, 300, 2)
    draw_tree(200, 275, 2)
    draw_tree(150, 200, 2)
    draw_tree(230, 70, 2)
    draw_tree(20, 150, 2)
    draw_tree(250, 180, 2)
    draw_tree(330, 150, 2)
    draw_tree(100, 100, 2)

    draw_tree(500, 260, 0.85)
    draw_tree(440, 250, 0.95)
    draw_tree(400, 220, 0.9)
    draw_tree(470, 210, 1)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")

    arcade.set_background_color(arcade.color.RED)

    arcade.schedule(draw, 1/10)

    arcade.run()


# Call the main function to get the program started.

main()

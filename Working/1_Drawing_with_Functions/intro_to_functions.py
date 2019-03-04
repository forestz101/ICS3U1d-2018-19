import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

green1 = (118, 171, 52)
green2 = (154, 189, 54)
# define your draw functions


def draw_cloud():
    arcade.draw_ellipse_filled(450, 450, 100, 80, arcade.color.WHITE)
    arcade.draw_ellipse_filled(550, 430, 60, 50, arcade.color.WHITE)
    arcade.draw_ellipse_filled(350, 430, 60, 50, arcade.color.WHITE)


def draw_rolling_hills():
    arcade.draw_ellipse_filled(450, 150, 150, 100, green2)
    arcade.draw_ellipse_filled(-100, -110, 700, 400, arcade.color.APPLE_GREEN)
    arcade.draw_ellipse_filled(700, -110, 400, 350, green1)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

    draw_cloud()
    draw_rolling_hills()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
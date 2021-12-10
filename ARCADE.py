import arcade

arcade.open_window(600, 600, "COMPLEX LOOPS")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

for r in range(10):
    for c in range(10):

        m = c * 20 + 210
        n = r * 20 + 210

        if (r+c)%2 == 0:
            arcade.draw_rectangle_filled(m , n , 12.5 , 12.5 , arcade.color.BLUE , 45)
        else:
            arcade.draw_rectangle_filled(m , n , 12.5 , 12.5 , arcade.color.RED , 45)

arcade.run()

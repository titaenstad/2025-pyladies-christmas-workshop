from n_waffle import n_heart_waffle
import turtlethread

space_between_waffle_centers = 500
waffle_heart_length = 150

needle = turtlethread.Turtle()

for i in range(1, 10):
    n_heart_waffle(heart_side_length=waffle_heart_length, num_hearts=i, needle=needle)
    with needle.jump_stitch(20):
        needle.forward(space_between_waffle_centers)

        if i % 3 == 0:
            # move needle to leftmost space on next line
            needle.right(90)
            needle.forward(space_between_waffle_centers)
            needle.right(90)
            needle.forward(3 * space_between_waffle_centers)
            needle.right(180)

needle.show_info()
needle.save("waffles.png")
needle.save("waffles.jef")
needle.visualise(scale=0.5)

import turtlethread


def make_braided_heart(
    square_part_length: int, num_bands: int, needle: turtlethread.Turtle
):
    needle.left(45)

    # Make parallell lines that point to the right side of the heart
    run_lines(
        square_part_length=square_part_length,
        num_bands=num_bands,
        needle=needle,
    )

    # Needle position after first run is dependent on number of bands being even or odd
    even_bands = num_bands % 2 == 0

    if even_bands:
        # Needle is in position, just rotate to correct direction
        needle.right(90)
    else:
        # Move needle down to west position and rotate
        with needle.jump_stitch(STITCH_LEN):
            needle.forward(square_part_length)
            needle.left(90)

    # Make parallell lines that point to the left side of the heart
    run_lines(
        square_part_length=square_part_length,
        num_bands=num_bands,
        needle=needle,
    )

    if even_bands:
        # Move needle to east position and rotate
        with needle.jump_stitch(STITCH_LEN):
            needle.forward(square_part_length)
            needle.left(90)
    else:
        needle.right(90)

    # Make heart half circles
    with needle.running_stitch(STITCH_LEN):
        needle.circle(radius=square_part_length / 2, extent=180)
        needle.right(90)
        needle.circle(radius=square_part_length / 2, extent=180)

    # Make top lines for braided look
    needle.left(90)
    band_width = square_part_length / num_bands
    every_other_line(
        start_with_line=True, line_length=band_width, num_lines=num_bands, needle=needle
    )
    needle.right(90)
    every_other_line(
        start_with_line=not even_bands,
        line_length=band_width,
        num_lines=num_bands,
        needle=needle,
    )


def every_other_line(
    start_with_line: bool, line_length: int, num_lines: int, needle: turtlethread.Turtle
):
    line = start_with_line
    for _ in range(num_lines):
        if line:
            with needle.running_stitch(STITCH_LEN):
                needle.forward(line_length)
        else:
            with needle.jump_stitch(STITCH_LEN):
                needle.forward(line_length)


def run_lines(square_part_length: int, num_bands: int, needle: turtlethread.Turtle):
    """Make long lines for criss cross pattern in braided heart"""
    band_width = square_part_length / num_bands
    go_left = True

    for _ in range(num_bands):
        if go_left:
            band_run_left(
                band_width=band_width, band_length=square_part_length, needle=needle
            )
        else:
            band_run_right(
                band_width=band_width, band_length=square_part_length, needle=needle
            )
        go_left = not go_left


def band_run_left(band_width: float, band_length: int, needle: turtlethread.Turtle):
    """Make one line for the criss cross of the braided heart, and position needle for next run."""
    with needle.running_stitch(STITCH_LEN):
        needle.forward(band_length)
    with needle.jump_stitch(STITCH_LEN):
        needle.left(90)
        needle.forward(band_width)
        needle.left(90)


def band_run_right(band_width: float, band_length: int, needle: turtlethread.Turtle):
    """Make one line for the criss cross of the braided heart, and position needle for next run."""
    with needle.running_stitch(STITCH_LEN):
        needle.forward(band_length)
    with needle.jump_stitch(STITCH_LEN):
        needle.right(90)
        needle.forward(band_width)
        needle.right(90)


STITCH_LEN = 20  # 2mm
waffle_heart_length = 150
num_bands = 3
needle = turtlethread.Turtle()

make_braided_heart(
    square_part_length=waffle_heart_length, num_bands=num_bands, needle=needle
)
needle.show_info()
needle.visualise(scale=1)

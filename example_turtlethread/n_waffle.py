import argparse

import turtlethread
from n_triangle import find_last_side


def make_n_part_heart(
    same_side_length: int,
    middle_side_length: int,
    rotate_angle: float,
    needle,
):
    needle.forward(same_side_length)
    needle.left(rotate_angle)
    needle.circle(radius=middle_side_length / 4, extent=180)
    needle.right(180)
    needle.circle(radius=middle_side_length / 4, extent=180)
    needle.left(rotate_angle)
    needle.forward(same_side_length)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Draw a Norwegian waffle (of n hearts).",
    )
    parser.add_argument(
        "n",
        type=int,
        nargs="?",
        default=5,
        help="How many hearts in the waffle (default: %(default)s)",
    )
    parser.add_argument(
        "same_side_length",
        nargs="?",
        type=int,
        default=150,
        help="Length of the two equal sides in each heart (default: %(default)s)",
    )
    return parser.parse_args()


def n_heart_waffle(heart_side_length: int, num_hearts: int, needle):
    middle_side_length = find_last_side(
        side_length=heart_side_length,
        number_of_triangles=num_hearts,
    )
    # inner angle between the two sides of equal length
    angle_v = 360 / num_hearts

    # angle between the unknown side and either of the known sides
    angle_u = (180 - angle_v) / 2

    rotate_angle = 180 - angle_u - 90

    with needle.running_stitch(20):  # 2mm
        for _ in range(num_hearts):
            make_n_part_heart(
                same_side_length=heart_side_length,
                middle_side_length=middle_side_length,
                rotate_angle=rotate_angle,
                needle=needle,
            )
            needle.left(180)


def main() -> None:
    args = parse_args()

    needle = turtlethread.Turtle()
    n_heart_waffle(
        heart_side_length=args.same_side_length, num_hearts=args.n, needle=needle
    )

    needle.show_info()
    needle.save(f"waffle_{args.n}.jef")
    needle.visualise(scale=0.5)


if __name__ == "__main__":
    main()

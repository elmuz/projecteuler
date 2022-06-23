def count_rectangles(width: int, height: int) -> int:
    counter = width * height  # start by summing all 1x1 rectangles
    for rec_w in range(1, width + 1):
        for rec_h in range(1, height + 1):
            if rec_h == 1 and rec_w == 1:
                continue  # skip 1x1 rectangles, already counted above
            counter += (width - rec_w + 1) * (height - rec_h + 1)
    return counter

assert count_rectangles(3, 2) == 18


if __name__ == '__main__':
    """
    Start with a 1x1 rectangle and try to enlarge it in width as long as
    the number of internal rectangles is lower than the target. Then increase
    the height of 1. Reduce the width until the number of rectangles is just
    under the target. Proceed this way until you have a square grid (when
    width is equal to height). By symmetry you have explored all possible
    grids.
    """
    width = 2
    height = 1
    max_width_found = False
    target = 2000000
    n_rect = 1
    best_approx = abs(n_rect - target)
    best_area = 1  # starting from 1x1 grid, with one rectangle
    while width > height:
        if n_rect < target and not max_width_found:
            # make the grid wider
            width += 1
        elif n_rect < target and max_width_found:
            # make the grid higher
            height += 1
        elif n_rect > target and not max_width_found:
            # reduce the width
            max_width_found = True
            width -= 1
            height += 1
        else:
            width -= 1
        n_rect = count_rectangles(width, height)
        delta = abs(n_rect - target)
        if delta < best_approx:
            best_area = width * height
            best_approx = delta
            print(f"Found a better approximation: {delta}. {n_rect} rectangles, for a {width}x{height} grid of area {width * height}.")

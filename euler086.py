INTEGER_SHORTEST_PATHS = {}


def is_a_pythagorean_triple(a: int, b: int) -> bool:
    c = (a ** 2 + b ** 2) ** 0.5
    if int(c) == c:
        return True
    else:
        return False


def has_integer_shortest_path(a: int, b: int, c: int) -> bool:
    """Let's unwrap the cuboid:
          _______________
         |               |
     ____|_______________|____
    |    |               |  * |
    |    |         .  *  |    |
    |    |   .  *        |    |
    |____|_*_____________|____|_ _ _
       F |*   -   .    _ |   .      :
         |___*___________| c = 3 _-_:
         |      *        |
         |        *      |
         |           *   | b = 5
         |_____________*_|
               a = 6      S

    Here: 6^2 + (3 + 5)^2 = 10^2
    We need to find face lengths which form a Pythagorean triple.
    If a >= b >= c, the shortest path is the one a^2 + (b + c)^2.
    """

    assert a >= b
    assert b >= c

    if is_a_pythagorean_triple(a, (b + c)):
        return True
    else:
        return False


def number_of_integer_shortest_paths(max_size: int) -> int:
    """It turns out that the solution is to explore all Pythagorean triples.
    A triple is defined with X > Y > Z where X^2 = Y^2 + Z^2.
    In the cuboid of edges a > b > c the shortest path would be the one of the
    form sqrt(a^2 + (b + c)^2).

    Try with a brute force approach first

    """
    counter = 0
    for a in range(1, max_size + 1):
        for b_plus_c in range(2, a * 2 + 1):
            if is_a_pythagorean_triple(a, b_plus_c):
                for b in range(min(a, b_plus_c - 1), 1, -1):
                    c = b_plus_c - b
                    if c > b:
                        break
                    counter += 1
                    
        # for b in range(1, a + 1):
        #     for c in range(1, b + 1):
        #         if has_integer_shortest_path(a, b, c):
        #             counter += 1
    return counter


if __name__ == "__main__":
    assert number_of_integer_shortest_paths(99) == 1975
    assert number_of_integer_shortest_paths(100) == 2060
    m = 1
    solutions = 0
    while solutions < 1e6:
        solutions = number_of_integer_shortest_paths(m)
        print(f"m: {m} -> solutions {solutions}")
        m += 1
    
    # Cheating... it was taking too much. So I went for trial and error
    # print(number_of_integer_shortest_paths(1820)) # -> 1006727
    # print(number_of_integer_shortest_paths(1819)) # -> 1000457
    # print(number_of_integer_shortest_paths(1818)) # -> 1000457
    print(number_of_integer_shortest_paths(1817)) # -> 999850
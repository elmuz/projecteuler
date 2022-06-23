from typing import Dict, List, Generator, Tuple

def triangle(n):
    return n * (n + 1) // 2


def square(n):
    return n * n


def pentagonal(n):
    return n * (3 * n - 1) // 2


def exagonal(n):
    return n * (2 * n - 1)


def heptagonal(n):
    return n * (5 * n - 3) // 2


def octagonal(n):
    return n * (3 * n - 2)


def is_linkable(a: int, b:int) -> bool:
    if str(a)[-2:] == str(b)[:2]:
        return True
    else:
        return False


def is_cyclic(l: List[int]) -> bool:
    if len(l) < 2:
        return False
    if any([len(str(i)) < 2 for i in l]):
        return False
    last_two_digits = str(l[0])[-2:]
    for n in l[1:]:
        if str(n)[:2] == last_two_digits:
            last_two_digits = str(n)[-2:]
        else:
            return False
    if str(l[0])[:2] != last_two_digits:
        return False
    return True


def iterlists(lists: Dict[int, List[int]]) -> Generator:
    for p, l in lists.items():
        for e in l:
            yield p, e

if __name__ == '__main__':

    n_3 = 1
    P_3 = triangle(n_3)
    n_4 = 1
    P_4 = square(n_4)
    n_5 = 1
    P_5 = pentagonal(n_5)
    n_6 = 1
    P_6 = exagonal(n_6)
    n_7 = 1
    P_7 = heptagonal(n_7)
    n_8 = 1
    P_8 = octagonal(n_8)

    P_3s = []
    while P_3 < 1000:
        n_3 += 1
        P_3 = triangle(n_3)
    P_3s.append(P_3)
    while P_3 < 10000:
        n_3 += 1
        P_3 = triangle(n_3)
        if P_3 < 10000:
            P_3s.append(P_3)

    P_4s = []
    while P_4 < 1000:
        n_4 += 1
        P_4 = square(n_4)
    P_4s.append(P_4)
    while P_4 < 10000:
        n_4 += 1
        P_4 = square(n_4)
        if P_4 < 10000:
            P_4s.append(P_4)

    P_5s = []
    while P_5 < 1000:
        n_5 += 1
        P_5 = pentagonal(n_5)
    P_5s.append(P_5)
    while P_5 < 10000:
        n_5 += 1
        P_5 = pentagonal(n_5)
        if P_5 < 10000:
            P_5s.append(P_5)

    P_6s = []
    while P_6 < 1000:
        n_6 += 1
        P_6 = exagonal(n_6)
    P_6s.append(P_6)
    while P_6 < 10000:
        n_6 += 1
        P_6 = exagonal(n_6)
        if P_6 < 10000:
            P_6s.append(P_6)

    P_7s = []
    while P_7 < 1000:
        n_7 += 1
        P_7 = heptagonal(n_7)
    P_7s.append(P_7)
    while P_7 < 10000:
        n_7 += 1
        P_7 = heptagonal(n_7)
        if P_7 < 10000:
            P_7s.append(P_7)

    P_8s = []
    while P_8 < 1000:
        n_8 += 1
        P_8 = octagonal(n_8)
    P_8s.append(P_8)
    while P_8 < 10000:
        n_8 += 1
        P_8 = octagonal(n_8)
        if P_8 < 10000:
            P_8s.append(P_8)

    P = {
        3: P_3s,
        4: P_4s,
        5: P_5s,
        6: P_6s,
        7: P_7s,
        8: P_8s,
    }

    missing_p = {4, 5, 6, 7, 8}
    for a in P_3s:
        for b_id, b in iterlists({p: P[p] for p in missing_p}):
            if not is_linkable(a, b):
                continue

            missing_p.remove(b_id)
            for c_id, c in iterlists({p: P[p] for p in missing_p}):
                if not is_linkable(b, c):
                    continue
                missing_p.remove(c_id)
                for d_id, d in iterlists({p: P[p] for p in missing_p}):
                    if not is_linkable(c, d):
                        continue
                    missing_p.remove(d_id)
                    for e_id, e in iterlists({p: P[p] for p in missing_p}):
                        if not is_linkable(d, e):
                            continue
                        missing_p.remove(e_id)
                        for f_id, f in iterlists({p: P[p] for p in missing_p}):
                            if not is_linkable(e, f) or not is_linkable(f, a):
                                continue
                            print(f"Found! The sum is {sum([a, b, c, d, e, f])}.")
                            print(f"3: {a}.")
                            print(f"{b_id}: {b}.")
                            print(f"{c_id}: {c}.")
                            print(f"{d_id}: {d}.")
                            print(f"{e_id}: {e}.")
                            print(f"{f_id}: {f}.")
                        missing_p.add(e_id)
                    missing_p.add(d_id)
                missing_p.add(c_id)
            missing_p.add(b_id)
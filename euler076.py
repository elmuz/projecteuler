lookup = {}
def find_combo(n: int) -> int:
    def _find_combo(n: int, min_i) -> int:
        if n < min_i:
            return 0
        if n == 1 and min_i == 1:
            return 1
        if (n, min_i) in lookup:
            return lookup[(n, min_i)]
        else:
            out = 0
            for i in range(min_i, n // 2 + 1):
                if (n - i, i) in lookup:
                    a = lookup[(n - i, i)]
                else:
                    a =  _find_combo(n - i, i)
                    lookup[(n - i, i)] = a
                out += a + 1
                lookup[(n, min_i)] = out
        return out

    return _find_combo(n, 1) - 1

print(find_combo(100))
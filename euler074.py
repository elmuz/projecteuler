def factorial(n: int) -> int:
    if n < 0:
        raise ValueError
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

fact = {
    n: factorial(n) for n in range(10)
}

def sum_factorials(n: int) -> int:
    total = 0
    for i in str(n):
        total += fact[int(i)]
    return total

chains = {}
chain_size = 60
counter_chains = 0
limit = 1000000
for i in range(limit + 1):
    if i in chains:
        continue
    n = i
    chain = [n]
    while True:
        next = sum_factorials(n)
        if next not in chain:
            chain.append(next)
            if next in chains:  # found in previous loops
                length = chains[next]
                chain.pop()
                while len(chain) > 0:
                    length += 1
                    m = chain.pop()
                    chains[m] = length
                    if length == chain_size:
                        counter_chains += 1
                break
        else:  # loop found
            next_idx = chain.index(next)
            loop_length = len(chain) - next_idx
            for idx, m in enumerate(chain[next_idx - 1::-1]):
                chains[m] = loop_length + idx + 1
                if loop_length + idx + 1 == chain_size:
                    counter_chains += 1
            for m in chain[next_idx:]:
                chains[m] = loop_length
                if loop_length == chain_size:
                    counter_chains += 1
            break
        n = next

print(f"Done! Found {counter_chains} chains of length {chain_size}.")
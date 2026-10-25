
from heapq import heappush, heappop

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)

def h(s):
    return sum(s[i] != goal[i] and s[i] != 0 for i in range(9))

pq = [(h(start), 0, start, [])]
visited = set()

while pq:
    f, cost, state, path = heappop(pq)

    if state in visited:
        continue
    visited.add(state)

    if state == goal:
        for s in path + [state]:
            for i in range(0, 9, 3):
                print(*s[i:i+3])
            print()
        break

    zero = state.index(0)

    for move in [-3, 3, -1, 1]:
        new = zero + move

        if not (0 <= new < 9):
            continue
        if move == -1 and zero % 3 == 0:
            continue
        if move == 1 and zero % 3 == 2:
            continue

        s = list(state)
        s[zero], s[new] = s[new], s[zero]
        s = tuple(s)

        if s not in visited:
            heappush(pq, (cost + 1 + h(s), cost + 1,
                          s, path + [state]))
else:
    print("No solution")

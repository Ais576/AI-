from heapq import heappush, heappop

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)

def h(state):
    return sum(state[i] != goal[i] and state[i] != 0
               for i in range(9))

pq = [(h(start), start, [])]
visited = set()

while pq:
    f, state, path = heappop(pq)

    if state == goal:
        print("Solution:", path + [state])
        break

    if state in visited:
        continue
    visited.add(state)

    zero = state.index(0)

    for move in [-3, 3, -1, 1]:
        new = zero + move

        if 0 <= new < 9 and not (
            move == -1 and zero % 3 == 0 or
            move == 1 and zero % 3 == 2
        ):
            s = list(state)
            s[zero], s[new] = s[new], s[zero]
            s = tuple(s)

            if s not in visited:
                heappush(pq, (len(path) + 1 + h(s),
                              s, path + [s]))

else:
    print("No solution")

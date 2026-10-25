def alphabeta(depth, node, maximizing, alpha, beta):
    if depth == 2:
        return tree[node]

    if maximizing:
        best = -999
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 999
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

tree = [3, 5, 6, 9]
print("Best value:", alphabeta(0, 0, True, -999, 999))

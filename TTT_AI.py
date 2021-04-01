def win_avoid(g, n):
    d1 = []
    d2 = []
    rows1 = []
    cols1 = []
    ds1 = []

    if n == 0:
        for r in range(3):
            for c in range(3):
                if g[r][c] == 0:
                    g[r][c] = 1
                    return g

    for i in range(3):
        cols = [r[i] for r in g]
        if sum(g[i]) == n:
            if abs(n) == 2:
                clear = g[i].index(0)
                g[i][clear] = 1
                return g
            elif g[i].count(0) == 2:
                rows1.append(i)

        if sum(cols) == n:
            if abs(n) == 2:
                clear = cols.index(0)
                g[clear][i] = 1
                return g
            elif cols.count(0) == 2:
                cols1.append(i)

        d1.append(g[i][i])
        d2.append(g[2 - i][i])

    if sum(d1) == n:
        if abs(n) == 2:
            clear = d1.index(0)
            g[clear][clear] = 1
            return g
        elif d1.count(0) == 2:
            ds1.append(1)

    if sum(d2) == n:
        if abs(n) == 2:
            clear = d2.index(0)
            g[2 - clear][clear] = 1
            return g
        elif d2.count(0) == 2:
            ds1.append(2)

    if abs(n) == 1:
        for r in rows1:
            for c in cols1:
                if g[r][c] == 0:
                    g[r][c] = 1
                    return g
            for d in ds1:
                if d == 1 and g[r][r] == 0:
                    g[r][r] = 1
                    return g
                elif d == 2 and g[r][2 - r] == 0:
                    g[r][2 - r] = 1
                    return g
        for c in cols1:
            for d in ds1:
                if d == 1 and g[c][c] == 0:
                    g[c][c] = 1
                    return g
                elif d == 2 and g[2 - c][c] == 0:
                    g[2 - c][c] = 1
                    return g


def ai(grid, level):
    cnt = sum(r.count(0) for r in grid)

    # win / avoid
    if win_avoid(grid, 2):
        return grid
    if level > 0 and win_avoid(grid, -2):
        return grid

    # strategy
    if cnt == 9:
        grid[1][1] = 1
    elif cnt == 8:
        if grid[1][1] == -1:
            grid[0][0] = 1
        else:
            grid[1][1] = 1
    elif cnt == 7:
        if grid[1].count(-1) == 1:
            grid[0][grid[1].index(-1)] = 1
        elif grid[0][1] == -1:
            grid[0][0] = 1
        elif grid[2][1] == -1:
            grid[2][0] = 1
        elif grid[0].count(-1) == 1:
            grid[2][grid[0].index(-1)] = 1
        elif grid[2].count(-1) == 1:
            grid[0][grid[2].index(-1)] = 1
    elif cnt == 6 and (grid[0][0] == grid[2][2] == -1 or grid[0][2] == grid[2][0] == -1):
        grid[0][1] = 1
    elif cnt == 6 and grid[1][1] == grid[2][2] == -1:
        grid[0][2] = 1
    elif level > 1 and win_avoid(grid, 1):
        return grid
    elif level > 1 and win_avoid(grid, -1):
        grid = win_avoid(grid, -1)
    elif win_avoid(grid, 0):
        return grid
    return grid


if __name__ == "__main__":
    print('Please do not bother me. Use TicTacToe_with_AI.py')

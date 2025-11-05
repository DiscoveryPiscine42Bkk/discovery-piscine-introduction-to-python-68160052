def checkmate(board):
    try:
        grid = [list(line) for line in board.splitlines() if line.strip() != ""]
        rows = len(grid)

        king = None
        for i in range(rows):
            for j in range(len(grid[i])):
                if grid[i][j] == "K":
                    king = (i, j)

        if not king:
            print("Fail")
            return

        kx, ky = king

        def in_bounds(x, y):
            return 0 <= x < rows and 0 <= y < len(grid[x])

        pawn_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in pawn_dirs:
            nx, ny = kx + dx, ky + dy
            if in_bounds(nx, ny) and grid[nx][ny] == "P":
                print("Success")
                return

        straight_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in straight_dirs:
            nx, ny = kx + dx, ky + dy
            while in_bounds(nx, ny):
                ch = grid[nx][ny]
                if ch != '.':
                    if ch in ('R', 'Q'):
                        print("Success")
                        return
                    break
                nx += dx
                ny += dy

        diag_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in diag_dirs:
            nx, ny = kx + dx, ky + dy
            while in_bounds(nx, ny):
                ch = grid[nx][ny]
                if ch != '.':
                    if ch in ('B', 'Q'):
                        print("Success")
                        return
                    break
                nx += dx
                ny += dy

        print("Fail")

    except Exception:
        print("Fail")
 
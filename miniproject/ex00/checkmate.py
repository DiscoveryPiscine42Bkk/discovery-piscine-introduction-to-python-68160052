def checkmate(board):
    try:
        # แปลง board เป็น grid (array 2D)
        grid = [list(line) for line in board.splitlines() if line.strip() != ""]
        if not grid:
            print("Error")
            return

        rows = len(grid)

        # หา King
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

        # Pawn
        pawn_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in pawn_dirs:
            nx, ny = kx + dx, ky + dy
            if in_bounds(nx, ny) and grid[nx][ny] == "P":
                print("Success")
                return

        # Rook / Queen (แนวตรง)
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

        # Bishop / Queen (แนวทแยง)
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

        # Knight
        knight_moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        for dx, dy in knight_moves:
            x, y = kx + dx, ky + dy
            if in_bounds(x, y) and grid[x][y] == "N":
                print("Success")
                return

        # ถ้าไม่มีตัวไหนขู่ King
        print("Fail")

    except Exception:
        print("Fail")
 
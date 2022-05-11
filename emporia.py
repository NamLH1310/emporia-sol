empty_place_count = 0
visited = set()
dy = [ 0,  0,  1, -1 ]
dx = [ 1, -1,  0,  0 ]
m, n = 0, 0
num_path_found = 0

def in_bound(y: int, x: int):
    global m, n
    return y >= 0 and y < m and x >= 0 and x < n

def backtrack(
        a: list[list[int]],
        cur_pos: tuple[int, int],
        ):
    global num_path_found, empty_place_count
    if len(visited) == empty_place_count:
        for i in range(4):
            y = dy[i] + cur_pos[0]
            x = dx[i] + cur_pos[1]
            if in_bound(y, x) and a[y][x] == 3:
                num_path_found += 1
                return
        return

    for i in range(4):
        y = dy[i] + cur_pos[0]
        x = dx[i] + cur_pos[1]
        if in_bound(y, x) and a[y][x] == 0 and (y, x) not in visited:
            visited.add((y, x))
            backtrack(a, (y, x))
            visited.remove((y, x))

def main():
    global m, n, empty_place_count
    m, n = list(map(int, input().split()))
    a = []
    for _ in range(m):
        row = list(map(int, input().split()))
        if len(row) != n:
            raise Exception("Wrong input format")
        for num in row:
            if num == 0:
                empty_place_count += 1
        a.append(row)

    start = (0, 0)
    for i, row in enumerate(a):
        for j, num in enumerate(row):
            if num == 2:
                start = (i, j)
                break

    backtrack(a, start)
    print(num_path_found)

if __name__ == '__main__':
    main()

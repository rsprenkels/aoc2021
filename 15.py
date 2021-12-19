import math

map = [[int(c) for c in line] for line in open('15.txt').read().splitlines()]
bottom_right = ((width := len(map[0])),(height := len(map)))
print(f'bottom_right: {bottom_right}')
cost = [[math.inf for _ in range(width)] for _ in range(height)]
cost[0][0] = 0
Q = [((0,0), [(0,0)])]
while Q:
    print(f'{len(Q):6} {cost[-1][-1]}')
    cur_loc, path = Q.pop()
    x,y = cur_loc
    for dx, dy in [(-1,0),(0,-1),(1,0),(0,1)]:
        if (nx := x+dx) >= 0 and nx < width and (ny := y+dy) >= 0 and ny < height:
            if (new_cost := cost[y][x] + map[ny][nx]) < cost[ny][nx] and (cost[-1][-1] == math.inf or new_cost < cost[-1][-1]):
                cost[ny][nx] = new_cost
                Q.append(((nx,ny), path + [(nx,ny)]))

print(f'part1: {cost[-1][-1]}')

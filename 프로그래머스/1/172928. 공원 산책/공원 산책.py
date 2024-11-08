def solution(park, routes):
    sx, sy = -1, -1
    
    move = {'E':(0, 1), 'W':(0, -1), 'S':(1, 0), 'N':(-1, 0)}
    
    # start 위치 확인
    for x, i in enumerate(park):
        for y, j in enumerate(i):
            if j == "S":
                sx, sy = x, y
                break

    # 이동 거리 적용
    for route in routes:
        location, m = route.split(' ')
        dist = int(m)
        dx, dy = move[location]

        nx, ny = sx, sy
        check = True

        for i in range(dist):
            nx += dx
            ny += dy

            # 벗어남
            if nx < 0 or ny < 0 or nx >= len(park) or ny >= len(park[0]) or park[nx][ny] == 'X':
                check = False
                break
        
        if check:
            sx, sy = nx, ny
        
    return [sx, sy]
# -*- coding: utf-8 -*-
from collections import deque

START_X, START_Y, LIMIT = 1000, 1000, 25
_sd_cache = {0: 0}

def sdig(n):
    n0 = abs(n)
    if n0 in _sd_cache:
        return _sd_cache[n0]
    s = 0
    x = n0
    while x:
        s += x % 10
        x //= 10
    _sd_cache[n0] = s
    return s

def solve():
    limit = LIMIT
    seen = set()
    q = deque()
    sdig_local = sdig
    if sdig_local(START_X) + sdig_local(START_Y) > limit:
        return 0
    q.append((START_X, START_Y))
    seen.add((START_X, START_Y))
    while q:
        x, y = q.popleft()
        # Раскрываем вручную 4 соседа
        nx = x + 1
        if (nx, y) not in seen and sdig_local(nx) + sdig_local(y) <= limit:
            seen.add((nx, y)); q.append((nx, y))
        nx = x - 1
        if (nx, y) not in seen and sdig_local(nx) + sdig_local(y) <= limit:
            seen.add((nx, y)); q.append((nx, y))
        ny = y + 1
        if (x, ny) not in seen and sdig_local(x) + sdig_local(ny) <= limit:
            seen.add((x, ny)); q.append((x, ny))
        ny = y - 1
        if (x, ny) not in seen and sdig_local(x) + sdig_local(ny) <= limit:
            seen.add((x, ny)); q.append((x,ny))
    return len(seen)

if __name__ == "__main__":
    print(solve())

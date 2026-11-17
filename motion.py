"""Existing point-robot paths. Objects are static blocked cells."""
from collections import deque


def point_path(width, height, blocked, start, goal):
    blocked = {tuple(cell) for cell in blocked}
    start, goal = tuple(start), tuple(goal)
    if start in blocked or goal in blocked:
        return None
    previous = {start: None}
    pending = deque([start])
    while pending:
        current = pending.popleft()
        if current == goal:
            path = []
            while current is not None:
                path.append(list(current))
                current = previous[current]
            return path[::-1]
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            other = current[0] + dx, current[1] + dy
            if (0 <= other[0] < width and 0 <= other[1] < height
                    and other not in blocked and other not in previous):
                previous[other] = current
                pending.append(other)
    return None

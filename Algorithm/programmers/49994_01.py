from asyncio import start_unix_server
import collections
from unittest import skip


def solution(dirs):
    answer = 0
    
    before_x = 0
    before_y = 0
    after_x = 0
    after_y = 0
    
    dirs = list(dirs)
    move = collections.defaultdict(list)

    for i in dirs:
        if i == 'U':
            if after_y >= 5:
                continue
            after_y += 1
        elif i == 'D':
            if after_y <= -5:
                continue
            after_y -= 1
        elif i == 'R':
            if after_x >= 5:
                continue
            after_x += 1
        elif i == 'L':
            if after_x <= -5:
                continue
            after_x -= 1

        if [after_x,after_y] not in move[str(before_x)+','+str(before_y)]:
            move[str(before_x)+','+str(before_y)].append([after_x, after_y])
            move[str(after_x)+','+str(after_y)].append([before_x, before_y])
            answer += 1
        before_x = after_x
        before_y = after_y
    
    return answer

dirs = "UUUUUUUDDDDDDD"
print(solution(dirs))
from collections import deque


num = int(input())

for i in range(num):
    n, m = map(int,input().split())
    deq = deque(map(int, input().split()))
    idx_deq = deque(range(0, n))

    count = 0

    while deq:
        if deq[0] == max(deq):
            count += 1
            deq.popleft()
            
            if idx_deq.popleft() == m:
                print(count)
                break
        else:
            temp_deq = deq.popleft()
            deq.append(temp_deq)
            temp_idx = idx_deq.popleft()
            idx_deq.append(temp_idx)
from collections import deque


def solution(bridge_length, weight, truck_weights):
  answer = 0
  
  deq = deque(truck_weights)
  deq2 = deque(0 for _ in range(bridge_length))
  total_weight = 0
  while deq2:
    answer += 1
    total_weight -= deq2.popleft()
    if deq:
      if total_weight + deq[0] <= weight:
        truck = deq.popleft()
        deq2.append(truck)
        total_weight += truck
      else:
        deq2.append(0)
      
  return answer

a = 2
b = 10
c = [7, 4, 5, 6]

print(solution(a, b, c))

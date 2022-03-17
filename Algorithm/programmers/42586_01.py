from collections import deque

def solution(progresses, speeds):
  answer = []
  
  deq = deque(progresses)
  deq2 = deque(speeds)

  while deq:
    count = 0
    while deq and deq[0] >= 100:
      deq.popleft()
      deq2.popleft()
      count += 1
    
    for i in range(len(deq)):
      deq[i] = deq[i] + deq2[i]
      
    if count > 0:
      answer.append(count)
  return answer
  

a = [93, 30, 55]
b = [1, 30, 5]

solution(a, b)
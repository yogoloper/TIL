def solution(N, stages):
    answer = []
    user_cnt = len(stages)

    
    rates = dict.fromkeys([i+1 for i in range(N)], 0)

    for stage in stages:
        if stage <= N:
            rates[stage] += 1
            
    for key in rates:

        cnt = rates[key]

        if cnt != 0:
            rates[key] =  cnt / user_cnt
        user_cnt = user_cnt - cnt

    rates = sorted(rates.items(), key=lambda x: x[1], reverse=True)

    for i in rates:
        answer.append(i[0])    
    
    return answer

n = 3
stages = [1, 1, 1]	
print(solution(n, stages))
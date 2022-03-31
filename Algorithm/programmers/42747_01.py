def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)

    h = 0

    for i, citation in enumerate(citations):
        if i >= citation:
            h = i
            break
    
    if h == 0:
        if max(citations) <= 0:
            answer = 0
        else:
            answer = len(citations)
    else:
        answer = len(citations[:h])
        

    return answer



citations = [3, 0, 6, 1, 5]	
citations = [3, 4, 5, 11, 15, 16, 17, 18, 19, 20]
citations = [1, 4]	
citations = [0, 1, 2]	
citations = [1, 3, 5, 7, 9, 11] 
citations = [20,21,22,23]
citations = [10, 10, 10, 10, 10]

citations = [1111, 2, 999, 777, 555, 10, 22]
citations = [1, 7, 0, 1, 6, 4] 
citations = [0] 
citations = [5] 
citations = [0, 0, 0, 0, 0]

print(solution(citations))
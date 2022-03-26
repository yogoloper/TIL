n = int(input())

score = []

# 입력값을 받아서 2차 배열로 만드는 과정
for _ in range(n):
    data = input().split()
    # 점수는 int 형태로 입력
    score.append( [data[0], int(data[1])] )

# 삽입 정렬이니까 첫번째 요소는 정렬 된것으로 취급하고
# 1번 인덱스부터 배열의 길이까지 반복
for i in range(1, len(score)):

    # i번째 인덱스부터 앞으로 이동하면서 비교
    for j in range(i, 0, -1):
        
        # 뒤의 요소가 앞의 요소보다 작을경우 교체
        if score[j][1] < score[j - 1][1]:
            score[j], score[j - 1] = score[j - 1], score[j]
        # 뒤의 요소가 앞의 요소보다 크다면 정렬된 상태이므로
        # 해당 요소의 정렬을 마침
        else:
            break

for i in score:
    print(i[0], end = ' ')
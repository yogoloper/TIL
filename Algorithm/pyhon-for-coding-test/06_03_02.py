n = int(input())

student = []

# 입력값을 받아서 딕셔너리 리스트 형태로 만드는 과정
for _ in range(n):
    name, score = input().split()
    # 데이터를 사용하기 쉽도록 딕셔너리에 키값을 별도로 지정
    # 점수는 int 형태로 저장
    student.append( {'name':name, 'score':int(score)} )

# 람다식을 통해서 student 리스트에 있는 딕셔너리들을
# 'score'의 값들을 통해서 정렬한다.
student = sorted(student, key=(lambda x: x['score']))

for i in student:
    print(i['name'], end = ' ')
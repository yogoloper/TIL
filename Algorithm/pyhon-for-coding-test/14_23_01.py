n = int(input())
student = []

for _ in range(n):
    a, b, c, d = map(str, input().split(' '))
    student.append({
      'name': a,
      'kor' : int(b),
      'eng': int(c),
      'math': int(d)
    })
    
student = sorted(student, key=lambda x: (-x['kor'], x['eng'], -x['math'], x['name']))
    
for i in range(len(student)):
    print(student[i]['name'])

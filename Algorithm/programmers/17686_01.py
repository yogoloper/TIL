import re
import string

from pkg_resources import split_sections

def solution(files):
    answer =[]
    dic = []
    for file in files:
        numbers = re.findall(r'[0-9]+', file)
        
        splits = file.split(numbers[0])
        
        if len(splits) == 0:
            head, tail = '', ''
        elif len(splits) == 1:
            head, tail = splits[0], ''
        else:
            head, tail = splits[0], splits[1]
            
        dic.append({
            'org': file,
            'head': head.lower(),
            'number': numbers[0],
            'tail': tail
        })
        
    
    dic = sorted(dic, key = lambda x : (x['head'], int(x['number']) ))
    for i in dic:
        answer.append(i['org'])

    return answer


files = ["img12.png", "img10.png", "img02.png","img1.png", "IMG01.GIF", "img2.JPG"]
files = ["O00321", "O49qcGPHuRLR5FEfoO00321"]
print(solution(files))


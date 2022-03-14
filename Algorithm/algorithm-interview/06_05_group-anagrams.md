# 애너그램 그룹

<!-- TOC -->

- [애너그램 그룹](#%EC%95%A0%EB%84%88%EA%B7%B8%EB%9E%A8-%EA%B7%B8%EB%A3%B9)
  - [문제](#%EB%AC%B8%EC%A0%9C)
  - [부연설명](#%EB%B6%80%EC%97%B0%EC%84%A4%EB%AA%85)
  - [예시](#%EC%98%88%EC%8B%9C)
  - [숙고 1](#%EC%88%99%EA%B3%A0-1)
  - [코드 1](#%EC%BD%94%EB%93%9C-1)
  - [숙고 2](#%EC%88%99%EA%B3%A0-2)
  - [코드 2](#%EC%BD%94%EB%93%9C-2)
  - [숙고 3](#%EC%88%99%EA%B3%A0-3)
  - [코드 3](#%EC%BD%94%EB%93%9C-3)

<!-- /TOC -->

## 문제
- https://leetcode.com/problems/group-anagrams/  
- 문자열 배열이 주어지면 Anagram을 함께 그룹화 한다.  
- 순서에는 제한이 없다.  

## 부연설명
- Anagram은 일종의 말장난으로 어떠한 단어의 문자를 재배열하여  
- 다른 뜻을 가지는 다른 단어로 바꾸는 것을 말한다.  

## 예시
``` python
Example 1:  
Input: strs = ["eat","tea","tan","ate","nat","bat"]  
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]  
Example 2:  
Input: strs = [""]  
Output: [[""]]  
Example 3:  
Input: strs = ["a"]  
Output: [["a"]] 
```

## 숙고 1
파이썬 문법이 익숙치 않아서 반복문을 두 개를 돌리고  
반복문 안에서 정렬을 여러 번 하고 하다보니 타임 리밋에 걸렸다..  

## 코드 1
``` python
class Solution(object):
    def groupAnagrams(self, strs):
        # 결과 배열(배열안에 배열을 담아서 반환)
        result = []
        # 한 번 나온 Anagram이 또 나왔는지 체크하기 위한 배열
        check = [0]*len(strs)

        
        # 문자열 리스트 반복
        for i in range(len(strs)):
            # 인덱스에 해당하는 문자열이 나왔다면 체크 배열 업데이트 하고
            # Anagram 그룹에 삽입
            if check[i] == 0:
                group = [strs[i]]
                check[i] = 1
            # 기존에 나온 문자열이라면 다음 인덱스로 동작
            else:
                continue

            # Anagram 의 기초가 된 단어를 만들기 위해
            # 단어를 오름차순으로 정렬
            temp_1 = ''.join(sorted(strs[i]))
            # i 인덱스에 1을 더한 곳 부터 끝까지 반복
            for j in range(i+1, len(strs)):
                # 비교할 단어도 오름차순으로 정렬
                temp_2 = ''.join(sorted(strs[j]))
                # 두 단어가 같고 비교하는 두 번째 단어가 나온적이 없다면
                if temp_1 == temp_2 and check[j] == 0:
                    # Anagram 그룹에 담아주고
                    # 나온적이 있다고 체크
                    group.append(strs[j])
                    check[j] = 1
            # Anagram 그룹을 결과 배열에 저장
            result.append(sorted(group))

        return result
```

## 숙고 2
- 키 값이 중복되지 않는 dictionary가 생각났다.

## 코드 2
``` python
class Solution(object):
  def groupAnagrams(self, strs):
      # 결과를 담을 딕셔너리를 선언
      anagrams = {}

      # 문자열 리스트 반복
      for str in strs:
          # 해당하는 단어를 오름차순으로 정렬해서
          # 키를 만듦
          key = ''.join(sorted(str))
          # 딕셔너리에 해당 키가 있으면 anagram 그룹 배열이 존재한다는 의미이므로
          # 해당 값에 새 단어를 append
          if key in anagrams:
              anagrams[key].append(str)
          # 딕셔너리에 해당키가 없으면
          # 키와 값을 새로 할당
          else:
              anagrams[key] = [str]
      # 이건 이쁘게 보이기 위해서 anagrams 그룹을 오름차순으로 정렬
      for key in anagrams:
          anagrams[key] = sorted(anagrams[key])
      # dictionary의 값들만 뽑아내면 이중리스트 형태로 반환
      return anagrams.values()
```

## 숙고 3
-  ~~2차까지도 나쁘지 않지만~~

## 코드 3
``` python
class Solution(object):
  def groupAnagrams(self, strs):
      # collections의 defaultdict()은
      # 인자로 주어진 객체(default-factory)의 기본값을
      # dictionary의 초기값으로 지정해준다.
      # 여기에서는 리스트를 초기값으로 지정
      anagrams = collections.defaultdict(list)
      for i in strs:
          anagrams[''.join(sorted(i))].append(i)
      return anagrams.values()
```

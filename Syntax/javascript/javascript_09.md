<!-- TOC -->

- [Array APIs](#array-apis)
  - [make a string out of an array](#make-a-string-out-of-an-array)
  - [make an array out of a string](#make-an-array-out-of-a-string)
  - [make this array look like this: [5, 4, 3, 2, 1]](#make-this-array-look-like-this-5-4-3-2-1)
  - [make new array without the first two elements](#make-new-array-without-the-first-two-elements)
  - [find a student with the score 90](#find-a-student-with-the-score-90)
  - [make an array of enrolled students](#make-an-array-of-enrolled-students)
  - [make an array containing only the students' scores](#make-an-array-containing-only-the-students-scores)
  - [check if there is a student with the score lower than 50](#check-if-there-is-a-student-with-the-score-lower-than-50)
  - [compute students' average score](#compute-students-average-score)
  - [make a string containing all the scores](#make-a-string-containing-all-the-scores)

<!-- /TOC -->

# Array APIs
``` javascript
// array-api.js

```

## make a string out of an array
- join()  
  배열의 모든 요소들을 구분자를 통해 문자열로 만든다.
``` javascript
// array-api.js

{
  const fruits = ['apple', 'banana', 'orange'];
  const result = fruits.join(',');
  console.log(result);
}
```
## make an array out of a string
- split()  
  문자열을 구분자를 통해 배열로 만든다.
``` javascript
// array-api.js

{
  const fruits = '🍎, 🥝, 🍌, 🍒';
  const result = fruits.split(',');
  console.log(result);
}
```

## make this array look like this: [5, 4, 3, 2, 1]
- reverse()  
  배열의 요소를 뒤집는다.
``` javascript
// array-api.js

{
  const array = [1, 2, 3, 4, 5];
  const result = array.reverse();
  console.log(result);
  console.log(array);
}
```

## make new array without the first two elements
- slice()  
  배열의 a요소부터 b요소-1까지 반환한다.
- vs splice()  
  splice는 본 배열을 수정하게 된다.
``` javascript
// array-api.js

{
  const array = [1, 2, 3, 4, 5];
  const result = array.slice(2, 5);
  console.log(result);
  console.log(array);
}
```

``` javascript 
// array-api.js

class Student {
  constructor(name, age, enrolled, score) {
    this.name = name;
    this.age = age;
    this.enrolled = enrolled;
    this.score = score;
  }
}
const students = [
  new Student('A', 29, true, 45),
  new Student('B', 28, false, 80),
  new Student('C', 30, true, 90),
  new Student('D', 40, false, 66),
  new Student('E', 18, true, 88),
];
```

## find a student with the score 90
- find()
``` javascript
// array-api.js

{
  // const result = student.find(function (student, index) {
  //   return sudent.score === 90;
  // });
  
  const result = students.find((student) => student.score === 90);
  console.log(result);

}
```

## make an array of enrolled students
- filter()  
  callback 함수가 true 인 요소들만 새로운 배열로 반환한다.
``` javascript
// array-api.js

{
  const result = students.filter((student) => student.enrolled);
  console.log(result);
}
```

## make an array containing only the students' scores
- map()  
  배열 안에 있는 원소 하나하나들을 새로운 원소로 변환한다.
``` javascript
// array-api.js

// result should be: [45, 80, 90, 66, 88]
{
  const result = students.map((student) => student.score);
  console.log(result);
}
```

## check if there is a student with the score lower than 50
- some()  
  배열의 요소중에서 하나라도 만족하는 조건이 있다면 true가 반환된다.
- every()  
  배열의 모든 요소들이 조건을 만족한다면 true가 반환된다.
``` javascript
// array-api.js

{
  console.clear();
  const result = students.some((student) => student.score < 50);
  console.log(result);

  const result2 = !students.every((student) => student.score >= 50);
  console.log(result2);
}
console.clear();
```

## compute students' average score
- reduce()  
  배열에 있는 모든 원소들의 값을 모아둘때 사용한다.
``` javascript
// array-api.js

{
  const result = students.reduce((prev, curr) => prev + curr.score, 0); // 0부터 시작
  console.log(result / students.length);
}
```

## make a string containing all the scores
``` javascript
// array-api.js

// result should be: '45, 80, 90, 66, 88'
{
  const result = students
    .map((student) => student.score) // 점수만 추출
    .filter((score) => score >= 50) // 50점 넘는 점수만 추출
    .join(); // 문자열로 합침
  console.log(result);
}

// Bonus! do Q10 sorted in ascending order
// result should be: '45, 66, 80, 88, 90'
{
  const result = students
    .map((student) => student.score) // 점수만 추출
    .sort((a, b) => b - a) // 내림차순 정렬
    .join(); // 문자열로 합침
  console.log(result);
}
```
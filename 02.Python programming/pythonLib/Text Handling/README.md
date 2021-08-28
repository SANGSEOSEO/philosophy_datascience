## 01장 텍스트 처리 서비스

파이썬은 텍스트 처리에 강한 언어이다. 문자열 자료형만 해도 강력한 기능들이 많지만 이에 못지 않게 유용한 라이브러리들도 다수 존재한다. 

이번 장에서는 텍스트 처리와 관련된 모듈들에 대해서 알아본다.

[Related Official Document ](https://docs.python.org/ko/3/library/textwrap.html)

### 01-01 textwrap.shorten - 문자열 말줄임

`textwrap.shorten` 함수는 문자열을 특정길이에 맞게 말줄임(...)을 할 때 사용하는 함수이다.

#### 문제

다음 문자열을 길이 15자리가 넘지 않도록 말줄임하여 표시하시오. (단, 길이가 15자리가 넘지 않을 경우에는 그대로 표시)

```
Life is too short, you need python
```

아래와 같이 코딩을 하고 수행

#### 풀이

```
import textwrap as tw

text =  "Life is too short, you need python."
print(tw.shorten(text, width=15))  
```

결과는 다음과 같다.

`width`옵션은 말줄임하고자 하는 자릿수

```
C:\projects\pylib\venv\Scripts\python.exe C:/projects/pylib/main.py
Life is [...]
```

이 때 문자열에 포함된 모든 연속된 공백 문자열은 단일 공백 문자열로 축약된다. 

그리고 매개변수 width에 전달된 길이만큼 문자열이 표시된다. 이 때 축약된 문자열을 의미하는 `[...]` 문자 역시 길이에 포함되며 줄여지는 문자열은 단어 단위로 길이에 맞게 생략된다.

> 문자열이 축약되더라도 문자열의 각 단어는 중간에 분리되지 않고 온전히 유지될 수 있게 축약된다.

한글 1개의 글자도 역시 길이 1로 계산됨을 유의

```
kor_text = "인생은 짧으니 파이썬이 필요해"
print(tw.shorten(kor_text, width=15))
```

결과는 다음과 같다.

```
인생은 짧으니 [...]
```

만약 축약 표시를 다른 형태로 바꾸고 싶다면...

```
import textwrap as tw

kor_text = "인생은 짧으니 파이썬이 필요해"
print(tw.shorten(kor_text,placeholder='...', width=15))
```

`placeholder`옵션으로 축약표시를 다른 형태로 변경 가능함.

### 01-02 textwrap.wrap - 문자열 줄바꿈

`textwrap.wrap` 함수는 문자열을 특정길이에 맞게 줄바꿈(wrapping)할 때 사용하는 함수이다. 문자열 래핑은 문자열이 너무 길어질 경우 특정 길이에서 줄바꿈을 하려고 할때 필요하다.

#### 문제

70바이트만 축약해서 보여주자.

```
import textwrap

long_text = "Life is too short. You need python" * 10

# shorten into 70bytes
print(textwrap.shorten(long_text, width=70, placeholder="..."))
```

#### 풀이

결과는 다음과 같다.

```
Life is too short. You need pythonLife is too short. You need...
```

#### 문제

70바이트씩 만큼 줄바꾸서 보여줄려면..

```
# wrap into 70bytes
result = textwrap.wrap(long_text,width=70)
print("70바이트만큼씩 줄바꿈", result)
```

#### 풀이

70바이트 만큼씩 줄바꿔서 찍어줌을 확인.결과값은 리스트로 리턴함을 알 수 있다.

```
70바이트만큼씩 줄바꿈 ['Life is too short. You need pythonLife is too short. You need', 'pythonLife is too short. You need pythonLife is too short. You need', 'pythonLife is too short. You need pythonLife is too short. You need', 'pythonLife is too short. You need pythonLife is too short. You need', 'pythonLife is too short. You need pythonLife is too short. You need', 'python']
```

> 문자열을 길이만큼 자르더라도 문자열의 각 단어는 중간에 분리되지 않고 온전히 유지될 수 있게 나뉘어진다.

```
#고정폭 문자열로 표시
print("\n".join(result))
```

[수행결과]

```
Life is too short. You need pythonLife is too short. You need
pythonLife is too short. You need pythonLife is too short. You need
pythonLife is too short. You need pythonLife is too short. You need
pythonLife is too short. You need pythonLife is too short. You need
pythonLife is too short. You need pythonLife is too short. You need
python
```

하지만 `textwrap.fill` 함수를 사용하면 위의 두가지 과정을 수행 할 필요가 없다.

```
#fill함수 사용하여 70바이트씩 줄바꿈하고 이것을 문자열로 표시
print(textwrap.fill(long_text, width=70))
```

수행결과 :

```
Life is too short. You need pythonLife is too short. You need
pythonLife is too short. You need pythonLife is too short. You need
pythonLife is too short. You need pythonLife is too short. You need
pythonLife is too short. You need pythonLife is too short. You need
pythonLife is too short. You need pythonLife is too short. You need
python
```

### 01-03 re - 정규표현식

정규 표현식(Regular Expressions)은 복잡한 문자열을 처리할 때 사용하는 기법으로, 파이썬만의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용한다.

파이썬에서 정규표현식을 사용하기 위해서는 `re` 모듈을 사용한다.

#### 문제

주민번호를 포함하고 있는 다음과 같은 텍스트가 있다.

```
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
```

이 텍스트에 포함된 모든 주민번호의 뒷자리를 `*` 문자로 변경해 보자.

#### 풀이

평범하게 이 문제를 해결하려면 다음과 같은 순서로 프로그램을 작성해야 한다.

```
1. 전체 텍스트를 공백 문자로 나눈다(split).
2. 나뉜 단어가 주민번호 형식인지 조사한다.
3. 단어가 주민번호 형식이라면 뒷자리를 `*`로 변환한다.
4. 나뉜 단어를 다시 조립한다.
```

이를 구현한 코드는 아마도 다음과 같을 것이다.

```
data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-"+"*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))
```

결과물

```/?
홍길동의 주민번호는 800905-******* 입니다. 
그리고 고길동의 주민번호는 700905-******* 입니다.
그렇다면 누가 형님일까요?
```

정규표현식을 사용하면?

```
import re

data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
```

결과는 위와 동일하다.

```
홍길동의 주민번호는 800905-******* 입니다. 
그리고 고길동의 주민번호는 700905-******* 입니다.
그렇다면 누가 형님일까요?
```

```
숫자6 + 하이픈문자(-) + 숫자7 (단, 숫자6은 괄호를 사용하여 그룹으로 지정되어있다.)
```

즉, 주민번호에 대응되는 정규표현식이다. 이 정규표현식을 `re.compile`로 만든 객체의 `sub`함수를 사용하면 이 정규표현식과 일치하는 문자열의 일부분을 `*`로 쉽게 바꿀수 있다.

<span style="color:red">pat.sub("\g<1>-*******", data)</span>이 부분이 문자열 변수 data에서 주민번호를 찾아 주민번호의 뒷부분만 `*`로 처리한다.

여기서 <span style="color:red">\g<1></span>의 의미는 정규표현식과 매치된 문자열에서 첫번째 그룹을 의미.

정규표현식에서 그룹을 지정하기 위해서는 <span style="color:red">(\d{6})</span>처럼 괄호로 묶어 그룹을 지정해야 한다.따라서 첫번째 그룹을 의미하는 <span style="color:red">\g<1></span>은 주민번호에서 바꾸지 않고 그대로 사용해야 하는 주민번호의 앞 부분을 의미한다.

#### 정규표현식의 기초 , 메타 문자

```
.^$*+?{}[]\|()
```

##### 문자 클래스 `[]`

문자클래스로 만들어진 정규식은 `[]`사이의 문자들과 매치라는 의미

| 정규식 | 문자열 | 매치여부 | 설명                                                         |
| ------ | ------ | -------- | ------------------------------------------------------------ |
| [abc]  | a      | Yes      | "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치           |
|        | before | Yes      | "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치      |
|        | dude   | No       | "dude"는 정규식과 일치하는 문자인 `a, b, c`중 어느 하나도 포함하고있지 않으므로 매치되지 않음 |

`[]`안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위(From - To)를 의미

6

> * [a-zA-Z] : 알파벳 모두 
>
> - [0-9] : 숫자

| 정규표현식 | 설명                                                         |
| :--------- | ------------------------------------------------------------ |
| \d         | 숫자와 매치. [0-9]와 동일한 표현식                           |
| \D         | 숫자가 아닌 것과 매치. [`^0-9`]와 동일한 표현식              |
| \s         | whitespace문자(space나 tab처럼 공백을 표현하는 문자)와 매치.`[\t\n\r\f\v]`와 동일한 표현식이다. 맨 앞의 빈칸은 공백 문자(space)를 의미 |
| \S         | whitespace문자가 아닌 것과 매치, `[^\t\n\r\f\v]`와 동일한 표현식 |
| \w         | 문자 + 숫자(alphanumeric)와 매치, [a-zA-Z0-9]와 일치         |
| \W         | 문자 + 숫자(alphanumeric)가 아닌 문자와 매치,`[^a-zA-Z0-9]`와 동일한 표현식 |


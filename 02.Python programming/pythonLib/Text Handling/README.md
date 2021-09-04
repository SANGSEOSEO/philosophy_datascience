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

###### Dot(.)

정규표현식의 Dot(.) 메타 문자는 줄바꿈 문자인 `\n`을 제외한 모든 문자와 매치됨을 의미

```
a.b  # a와 b사이에 줄바꿈 문자를 제외한 어떤 문자가 들어가도 모두 매치
```

```
a[.]b # a와 b사이에 Dot(.)문자가 있으면 매치. "a.b"와 동일한 표현식
```

###### 반복(*)

```
ca*t # `*`바로 앞의 문자 a가 0번 이상 반복되면 매치됨
```

| 정규식 | 문자열 | 매치여부 | 설명                                   |
| ------ | ------ | -------- | -------------------------------------- |
| ca*t   | ct     | Yes      | "a"가  0번 반복되어 매치됨             |
|        | cat    | Yes      | "a"가 0번 이상 반복되어 매치(1번 반복) |
|        | caaat  | Yes      | "a"가 0번 이상 반복되어 매치(3번 반복) |

###### 반복(+)

`+`는 최소 1번 이상 반복될때 사용.즉, `*`반복횟수 0부터라면 `+`는 반복횟수는 1부터인 것이다.

```
ca+t # `+`문자 바로 앞에 있는 문자가 1번이상 반복되면 매치
```

|      | 문자열 | 매치여부 | 설명                                   |
| ---- | ------ | -------- | -------------------------------------- |
| ca+t | ct     | No       | "a"가  0번 반복되어 매치되지 않음      |
|      | cat    | Yes      | "a"가 1번 이상 반복되어 매치(1번 반복) |
|      | caaat  | Yes      | "a"가 3번 이상 반복되어 매치(3번 반복) |

###### 반복({m, n}, ?)

* {m}

  ```
  ca{2}t # `a`가 2번 반복되면 매치
  ```

  | 정규식 | 문자열 | 매치 여부 | 설명                               |
  | ------ | ------ | --------- | ---------------------------------- |
  | ca{2}t | cat    | No        | `a`가 1번만 반복되어 매치되지 않음 |
  |        | caat   | Yes       | `a`가 2번 반복되어 매치됨          |

* {m, n}

```
ca{2, 5}t # `a`가 2번 이상 5번이하 반복되면 매치
```

| 정규식    | 문자열  | 매치 여부 | 설명                               |
| --------- | ------- | --------- | ---------------------------------- |
| ca{2, 5}t | cat     | No        | `a`가 1번만 반복되어 매치되지 않음 |
|           | caat    | Yes       | `a`가 2번 반복되어 매치됨          |
|           | caaaaat | Yes       | `a`가 5번 반복되어 매치됨          |

* `?`

```
ab?c # b가 0~1번 사용되면 매치됨
```

| 정규식 | 문자열 | 매치 여부 | 설명                    |
| ------ | ------ | --------- | ----------------------- |
| `ab?c` | `abc`  | Yes       | `b`가 1번 사용되어 매치 |
|        | `ac`   | Yes       | b가 0번 사용되어 매치   |

#### 파이썬에서 정규 표현식을 지원하는 re모듈

```
import re
p = re.compile("ab*")  # re.compile을 사용하여 정규 표현식을 컴파일
```

#### 정규식을 사용한 문자열 검색

| 메서드       | 목적                                                         |
| ------------ | ------------------------------------------------------------ |
| `match()`    | 문자열의 **처음부터 정규식과 매치되는지 조사**한다.          |
| `search()`   | **문자열 전체를 검색**하여 정규식과 매치되는지 조사한다.     |
| `findall()`  | 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴     |
| `finditer()` | 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다. |

* `match`

우선 다음과 같은 패턴을 만들고.

```/
import re


p = re.compile('[a-z]+')  # 문자가 1번 이상 나오면 적합

m = p.match("python")
print(m)
```

결과는?

```/
<re.Match object; span=(0, 6), match='python'>
```

그럼 이 결과는?

```
m = p.match("3 python")
print(m)
```

```
None
```

결과는 None이다. 숫자가 있기 때문에 매치되지 않음

파이썬의 정규 표현식 로직의 흐름은 다음과 같다.

```
p = re.compile(정규표현식)
m = p.match("조사할 문자열")

if m:
    print("Match Found:", m.group())
else:
    print("No match")
```

* `search`

  ```
  m = p.search("python")
  print("re.search()", m)
  ```

  [결과]

  ```
  re.search() <re.Match object; span=(0, 6), match='python'>
  ```

  숫자가 같이 있는 경우는?

  ```
  m = p.search("3 python")
  print("숫자가 같이 있는 경우: ", m)
  ```

  [결과]

  매치됨을 확인할 수 있다.

  ```
  숫자가 같이 있는 경우:  <re.Match object; span=(2, 8), match='python'>
  ```

* `findall`

  ```
  # findall
  result = p.findall("life is too short")
  print("findall : ", result)
  ```

* `finditer`

  ```
  # finditer
  result = p.finditer("life is too short")
  print("finditer() result : ", result)
  for r in result:
      print(r)
  ```

  결과는 다음과 같다.

  ```
  <re.Match object; span=(0, 4), match='life'>
  <re.Match object; span=(5, 7), match='is'>
  <re.Match object; span=(8, 11), match='too'>
  <re.Match object; span=(12, 17), match='short'>
  ```

  ##### match객체의 메소드

  | 메서드  | 목적                                                   |
  | ------- | ------------------------------------------------------ |
  | group() | 매치된 문자열을 돌려준다.                              |
  | start() | 매치된 문자열의 시작 위치를 리턴                       |
  | end()   | 매치된 문자열의 끝 위치를 리턴                         |
  | span()  | 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다. |

  [사용 예]       

```
import re

p = re.compile('[a-z]+')
m = p.match("python")
print(m.group())  # 매치되는 문자열 리턴
print(m.start())  # match메소드는 항상 문자열의 시직부터 조사하므로.
print(m.end())
print(m.span())
```

결과는 다음과 같다.

```
<re.Match object; span=(0, 4), match='life'>
<re.Match object; span=(5, 7), match='is'>
<re.Match object; span=(8, 11), match='too'>
<re.Match object; span=(12, 17), match='short'>
```

만약, search메소드를 사용했다면?

```
import re
p = re.compile("[a-z]+")
m = p.search("3 python")
print(m.group())
print(m.start())
print(m.end())
```

###### 컴파일 옵션

정규식을 컴파일 할때 다음 옵션을 사용 가능함.

| 욥션 이름    | 약어 | 설명                                                         |
| ------------ | ---- | ------------------------------------------------------------ |
| `DOTALL`     | s    | dot문자(`.`)가 줄바꿈 문자를 포함하여 모든 문자와 매치한다.  |
| `IGNORECASE` | I    | 대, 소문자에 관계없이 매치한다.                              |
| `MULTILINE`  | M    | 여러 줄과 매치한다.(`^`, `$` 메타 문자의 사용과 관계가 있는 옵션) |
| `VERBOSE`    | X    | verbose모드를 사용(정규식을 보기 편하게 만들 수 도 있고 주석등을 사용할 수도 있다.) |

* `re.DOTALL`

```
import re
p = re.compile("a.b")
m = p.match("a\nb")
print("DOTALL : ", m)
```

`\n`은 메타문자 `.`와 매치되지 않아서 결과는 `None`를 리턴한다.

```
DOTALL :  None
```

`DOTALL`옵션을 사용하면 `\n`문자와 매치가 가능하며, 여러불로 이루어진 문자열에서의 검색이 가능하게 하기 위해서 사용 가능함

```
p1 = re.compile("a.b", re.DOTALL)
m1 = p1.match("a\nb")
print(m1)
```

결과는 아래 화면을 참조

```8 
<re.Match object; span=(0, 3), match='a\nb'>
```

* `re.IGNORECASE 혹은 re.I`

  대소문자와 상관없이 매치

  ```
  p = re.compile("[a-z]", re.IGNORECASE)
  m = p.match("python")
  print(m)
  
  m = p.match("Python")
  print(m)
  
  m = p.match("PYTHON")
  print(m)
  ```

  결과는 다음과 같다.

  ```
  <re.Match object; span=(0, 1), match='p'>
  <re.Match object; span=(0, 1), match='P'>
  <re.Match object; span=(0, 1), match='P'>
  ```

* `re.MULTILINE 혹은 re.M`

  ```
  import re
  p = re.compile("^python\s\w+") # python으로 시작하고 공백다음에 단어가 1개 이상 있는 문자열만 매치
  
  data = """python one
  Life is too short
  python two
  you need python
  python three"""
  
  print(p.findall(data))
  ```

  `^`메타 문자에 의해 `python`이라는 문자열을 사용한 첫번째 줄만 매치된다.

  ```
  ['python one']
  ```

  하지만 `^`메타 문자를 문자열 전체의 처음이 아니라 각 라인의 처음으로 인식시키고 싶다면 즉, 멀티라인에 걸쳐서 해당 메타문자가 매치됨을 적용하고싶다.

  ```
  print(p.findall(data))
  
  p = re.compile("^python\s\w+", re.MULTILINE)
  multiline = p.findall(data)
  print("re.MULTILINE적용: ", multiline)
  ```

  `^`메타 문자가 각 라인마다 적용된다.

  ```
  re.MULTILINE적용:  ['python one', 'python two', 'python three']
  ```

* `VERBOSE 혹은 X`

  정규식을 주석 또는 줄 단위로 구분할 수 있게 해준다.(가독력을 높여준다고 이해하면 될듯함)

  ```
  charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
  ```

  위 정규식을 아래와 같이 쉽게 해주는 역할

  ```
  charref = re.compile(r"""
   &[#]                # Start of a numeric entity reference
   (
       0[0-7]+         # Octal form
     | [0-9]+          # Decimal form
     | x[0-9a-fA-F]+   # Hexadecimal form
   )
   ;                   # Trailing semicolon
  """, re.VERBOSE)
  ```

* `백슬래스 문제`

  정규표현식 사용시, `\`을 그대로 사용하면 의도한 대로 매치가 되지 않으므로 이스케이프 처리를 해야 한다.

  `\section`이라는 문자열을 찾고자 하는 하는 것이 아래 정규식의 의도이다.

  ```
  \section
  ```

  하지만, `\s`문자가 whitespace로 인식되기 때문에 의도한대로 메치가 되지 않는다.

  이런 경우에는 escape처리를해야 한다.

  ```
  \\section
  ```

  ```
  p = re.compile("\\section")
  ```

  그런데 여기에서 또 하나의 문제가 발견된다.위 처럼 정규식을 만들어 컴파일하면 실제 파이썬 정규식 엔진에는 파이썬리터럴 규칙에 따라 `\\`가 `\`로 변경되어 `\section`이 전달된다.

  그러므로 결국 정규식 엔진에 `\\`문자를 전달하려면 파이썬은 `\\\\`처럼 백슬래시를 4개나 사용해야 한다.

  하지만 너무 복잡하다.

  위와같이 `\`를 사용해야만 하는 정규표현식이 계속 반복된다면 가독성이 떨어질것이 때문에 이런 문제로 인해 파이썬 정규식에는 `Raw String`규칙이 생겨나게 되었다.

  ```
  p = re.compile(r'\\section)
  ```

  

#### 메타문자

앞에서 살펴본 메타문자 `+, *, [], {}`등의 메타 문자는 메치가 진행될 때 현재 매치되고 있는 문자열의 위치가 변경된다(보통 소비된다고 표현). 하지만  이와 달리 문자열을 소비시키지 않는 메타문자도 있다. 

이번에는 이런 문자열 소비가 없는(zero-width assertions)메타 문자에 대허 살펴본다.

* `|` 

  `|`메타 문자는 `or`과 동일한 의미로사용

  ```
  import re
  
  p = re.compile('Crow|Servo')
  m = p.match("CrowHello")
  print("Or match : ", m)
  ```

  결과는 다음과 같다.

  ```
  Or match :  <re.Match object; span=(0, 4), match='Crow'>
  ```

* `^`

  `^` 메타 문자는 문자열의 맨 처음과 일치함을 의미.

  ```
  # `^`메타 문자
  print(re.search("^Life", "Life is too short"))
  print(re.search("^Life", "My Life"))
  ```

  ```
  <re.Match object; span=(0, 4), match='Life'>
  None
  ```

  `^Life`정규식은 Life문자열이 처음에 온 경우에만 매치하지만 처음 위치가 아닌 경우에는 매치되지 않음을 알 수 있다.

* `$`

  `$` 메타 문자는 `^` 메타 문자와는 반대의 경우이다. 즉, `$`는 문자열의 끝과 매치됨을 의미

  ```
  # `$` 메타 문자
  print(re.search("short$", "Life is too short"))
  print(re.search("short$", "Life is too short. you need python"))
  ```

  ```
  <re.Match object; span=(12, 17), match='short'>
  None
  ```

* `\A`

  `\A` 는 문자열의 처음과 매치됨을 의미. `^` 메타 문자와 동일한 의미이지만 `re.MULTILINE`옵션을 사용할 경우에는 다르게 해석된다.

  `re.MULTILINE`옵션을 사용할 경우엔 `^`은 각 줄의 문자열의 처음과 매치되지만 `\A`는 줄과 상관없이 전체 문자열의 처음하고만 매치된다.

* `\Z`

  `\Z`는 문자열의 끝과 매치됨을 의미. 이것 역시 `\A`와 동일하게 `re.MULTILINE`옵션을 사용할 경우 `$`메타 문자와는 달리 전체 문자열의 끝과 매치된다.

* `\b`

  `\b`는 단어 구분자(Word boundary) 이다. 보통 단어는 whitespace에 의해 구분된다.

  ```
  # `\b`메타 문자
  p = re.compile(r'\bclass\b')
  print(p.search("no class at all"))
  print(p.search("the declassified algorithm"))
  ```

  ```
  <re.Match object; span=(3, 8), match='class'>
  None
  ```

  `class`란 단어 앞 뒤로 공백이 있으면 무조건 매치

  ```
  print(p.search("one subclass is"))
  >>> None
  ```

* `\B`

  `\B` 메타 문자는 `\b`메타 문자와 반대의 경우이다. 즉, whitespace로 구분된 단어가 아닌 경우에만 매치된다.

  ```
  # `\B`메타 문자
  p = re.compile(r"\Bclass\B")
  print(p.search("no class at all"))
  print(p.search("the declassified algorithm"))
  print(p.search("one subclass is"))
  ```

  ```
  None
  <re.Match object; span=(6, 11), match='class'>
  None
  ```

  

#### 그룹핑

ABC문자열이 계속해서 반복되는지 조사하는 정규식을 작성해야 한다면 어떻게 해야 할까?

그루핑을 이용해 보자

```
(ABC)+
```

그룹을 만들어 주는 메타 문자가 바로 `()`이다.

```
# 그루핑
p = re.compile("(ABC)+")  # `ABC`가 반복되면 매치
m  = p.search("ABCABCABC OK?")
print("Grouping result : ", m)
print("Result : {}".format(m.group()))
```

```
Grouping result :  <re.Match object; span=(0, 9), match='ABCABCABC'>
Result : ABCABCABC
```

```
data = "park 010-1234-1234"
p = re.compile(r"\w+\s+\d+[-]+\d+[-]\d+")  # '이름 + " " + 전화번호'형태의 문자열을 찾는 정규식
m = p.search(data)
print(m)
```

결과는 다음과 같다.

```
<re.Match object; span=(0, 18), match='park 010-1234-1234'>
```

그런데 `이름` 부분만 뽑아내려 한다면?

```
p = re.compile(r"(\w+)\s+((\d+)[-]+\d+[-]\d+)")
m = p.search(data)
print(m.group())
```

```
<re.Match object; span=(0, 18), match='park 010-1234-1234'>
park 010-1234-1234
```

| group(인덱스) | 설명                          |
| ------------- | ----------------------------- |
| group(0)      | 매치된 전체 문자열            |
| group(1)      | 첫번째 그룹에 해당하는 문자열 |
| group(2)      | 두번째 그룹에 해당하는 문자열 |
| group(n)      | n번째 그룹에 해당하는 문자열  |

```
# 이름만 뽑아오기
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search(data)
print(m.group(1))
```

결과

```
park
```

```
# 전화번호 뽑아오기
p = re.compile((r"(\w+)\s+(\d+[-]\d+[-]\d+)"))
m = p.search(data)
print(m.group(2))
```

결과

```
010-1234-1234
```

자, 이번에 국번만 뽑아오고자 한다면?

```
# 국번만 뽑아오기
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search(data)
print(m.group(3))

# 결과는 다음과 같다.
>>> 010        
```

##### 그루핑된 문자열 재참조

그룹의 또 하나 좋은 점은 한 번 그루핑한 문자열을 재참조가 가능하다는 점이다.

다음 예를 보자

```
p = re.compile(r"(\b\w+)\s+\1")  # 단어 앞에 공백이 있고 1개이상의 동일한 단어가 반복되면 매칭
m= p.search("Paris in the the spring")
print(m.group())
```

`\1`이 재참조 문자이며 정규식의 그룹중 첫번째 그룹을 가져오란  의미.

```
#결과
the the
```

> 두번째 그룹을 참조하려면 `\2`를 사용하면 된다.

##### 그루핑된 문자열에 이름 붙히기

정규식안에 그룹이 무척 많아지거나 혹은 정규식에 그룹이 많은데 정규식이 수정되면서 그룹을 참조하는 모든 프로그램도 다 수정해주어야 하는 문제가 발생한다. 

이런 경우엔 인덱스를 이름으로 참조할  수 있다면 ..정규식을 그룹을 만들때 그룹 이름을 지정할 수 있게 했다.

> (?P<name>\w+\s+((\d+)[-]\d+[-]\d+))

```
# 그룹에 이름 지정
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-9999-0099")
print(m.group("name"))
```

```
park
```

정규식안에서 재참조

```
# 그룹 이름을 사용후 정규식안에서 재참조하기
p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
print(p.search("Paris in the the spring").group())
```

```
the the
```

#### 전방탐색

```
# 전방탐색
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
```

결과는 다음과 같다.

```
http:
```

만약, `http:`라는 검색 결과에서 `:`를 제외하고 출력하려면 어떻게 해야 할까?  그루핑은 추가로 할 수 없다는 조건까지 더해진다면

이럴때 사용 할 수 있는 것이 전방탐색이다.

전방탐색에는 긍정과 부정의 2종류가 있고 다음과 같이 표현한다.

| 정규식  | 종류            | 설명                                                         |
| ------- | --------------- | ------------------------------------------------------------ |
| (?=...) | 긍정형 전방탐색 | `...`에 해당하는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다. |
| (?!...) | 부정형 전방탐색 | `...`에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다. |

##### 긍정형 전방 탐색

긍8정형 전방탐색을 사용하면 `http:`의 결과를 `http`로 바꿀수 있다.

```
# 긍정형 전방탐색
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())
```

정규식 중 `:`에 해당하는 부분에 긍정형 전방탐색 기법을 적용하여 `(?=:)`으로 변경하였다. 이렇게 되면 기존 정규식과 검색에서는 동일한 효과를 발휘하지만 `:`에 해당하는 문자열이 정규식 엔진에 의해 소비되지 않아(검색에는 포함되지만 검색결과에서는 제외됨) 검색결과에서는 `:`이 제거된 후 돌려주는 효과가 있다.

<결과>

```
http
```

이번에는 다음 정규식을 한 번 보자

> `.*[.].*$`

이 정규식은 `파일이름 +. + 확장자` 를 나타내는 정규식이다. 이 정규식은 `foo.bar, autoexec.bat, sendmail.cf`와 같은 형식의 파일과 매치될것이다.

이 정규식에 확장자가 `.bat`인 파일은 제외해야 한다는 조건이 추가된다고 해보자.

> `.*[.][^b].*$`

위의 정규 표현식은 `foo.bar`라는 파일마저 걸러낸다.

##### 부정형 전방탐색

> `.*[.](?!bat$).*$`

위의 정규식은 확장자가 `.bat`가 아닌 경우만 통과된다는 의미. `.exe`도 같이 걸려야 된다면..

> `.*[.](?!bat$ | exe$).*$`

#### 문자열 바꾸기

`sub`메서를 사용하면 정규식과 매치되는 부분을 다른 문자열로 바꿀 수 있다.

```
# 문자열 바꾸기
p = re.compile("blue|white|red")
m = p.sub("colour", "blue socks and red shoes")  # blue 혹은 red라는 문자열을 colour로 바꾼다.
print(m)
```

결과는 다음과 같다.

```
colour socks and colour shoes
```

딱 한번만 바꾸고 싶은 경우는?

```
p = re.compile("blue|white|red")
m = p.sub("colour", "blue socks and red shoes",  count=1) # 세번째 매개변수로 count를 넘겨주기
print(m)
```

결과는 바로 다음과 같다.

```
colour socks and red shoes
```

이와 유사한 `subn`도 있는데 차이점을 보자

```
p = re.compile("blue|white|red")
m = p.subn("colour", "blue socks and red shoes")
print(m)
```

```
('colour socks and colour shoes', 2)
```

위와 같이 변경된 결과와 갯수를 튜플로 반환한다는 차이점이 있다.

##### sub메소드를 사용할 때 참조 구문 사용하기

```
 p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
 print(p.sub("\g<phone>\g<name>", "park 010-1234-5690"))
```

```
010-1234-5690park
```

위 예는 `이름 + 전화번호`의 문자열을 `전화번호+이름`으로 바꾸는 예로서, `sub`의 바꿀 문자열 부분에 `\g<그룹이름>`을 사용하면 정규식의 그룹 이름을 참조할 수 있게 된다.

```
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
 print(p.sub("\g<2> \g<1>", "park 010-1234-5690"))
```

```
010-1234-5690 park
```

##### `sub`메서드이 매개변수로 함수 넣기

```
def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r"\d+")
m = p.sub(hexrepl, "call 65490 for printing, 49152 for use code.")
print(m)
```

결과는 다음과 같다.

```
call 0xffd2 for printing, 0xc000 for use code.
```

#### Greedy v.s Non-Greedy

정규식에서 Greedy(탐욕스러운)란 어떤 의미일까?

```
s = "<html><head><title>Title</title>"
print(len(s))

print(re.match("<.*>", s).span())
print(re.match("<.*>", s).group())
```

`<.*>`정규식의 매치 결과로 <html>문자열을 돌려주기를 기대했을 것이다. 하지만 `*`메타 문자는 매우 탐욕스러워 매치할 수 있는 최대한의 문자열인 <html><head><ittle>Title</title>문자열을 모두 소비해 버렸다. 

어떻게 하면 이 탐욕스러움을 제한하고 <html>문자열 까지만 소비하도록 막을 수 있을까?

다음과 같이 non-greedy문자인 `?`를 사용하면 `*`의 탐욕을 제한 할 수 있다.

```
print(re.match("<.*?>", s).group())
```

결과는 다음과 같다.

```
<html>
```

non-greedy문자인 `?`는 `*?, +?, ??, {m,n}?`와 같이 사용 할 수 있다.

가능한 한 가장 최소한의 반복을 수행하도록 도와주는 역할을 한다.

## 참조문헌

* https://wikidocs.net/1669
* https://docs.python.org/ko/3/library/re.html


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

  


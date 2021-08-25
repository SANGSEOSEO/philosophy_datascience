## 01장 텍스트 처리 서비스

파이썬은 텍스트 처리에 강한 언어이다. 문자열 자료형만 해도 강력한 기능들이 많지만 이에 못지 않게 유용한 라이브러리들도 다수 존재한다. 

이번 장에서는 텍스트 처리와 관련된 모듈들에 대해서 알아본다.

[Related Official Document](https://docs.python.org/ko/3/library/textwrap.html)

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


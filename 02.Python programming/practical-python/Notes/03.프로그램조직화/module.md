# 모듈

이번 섹션은 모듈의 개념을 소개하고 여러 파일에 걸쳐 함수를 다룬다.

### 모듈과 임포트 

모든 파이썬 소스파일은 모듈이다.

```python
# foo.py
def grok(a):
    ...
def spam(b):
    ...
```

`import`문은 모듈을 적재하고 실행(execute)한다.

```python
import foo
a = foo.grok(2)
b = foo.spam('Hello')
```

### 네임스페이스(namespaces)

모듈은 이름이 있는 변수들의 컬렉션이며, 종종 **네임스페이스**라고도 부른다. 이름은 모두 글로벌 변수이며 함수는 소스 파일에 정의된다. 임포트한 뒤, 모듈명은 프리픽스(prefix)로 사용된다. **네임스페이스**라고 부르는 것은 그 때문이다.

```python
import foo
a = foo.grok(2)
b = foo.spam('Hello')
```

모듈명은 파일명과 직접 연관된다(foo --> foo.py)

### 글로벌정의

`global scope`에 존재하는 모든것은 `모듈 네임스페이스`에 존재한다. `x`라는 동일한 변수명을 정의하고있는 두 개의 모듈을 고려해보자

```python
# foo.py
x = 42
def grok(x):
    ....
```

```python
#bar.py
x = 37
def spam(x)
```

위의 경우를 보면 `x`는 서로 다른 변수를 참조한다.하나는 `foo.x`그리고 다른 하나는 `bar.x`이다.

위의 두 변수를 서로 다른 `namespace`안에서 같은 이름을 사용 할 수 있음을 보여준다.

`Modules are isolated`라는 의미는 `모듈은 서로 독립적인 네임스페이스를 갖는다` 는 의미.

### 환경이라는 의미로서의 모듈

모듈은 모듈안에 정의된 모든 함수 및 변수를  감싸는 환경을 제공한다는 의미.

```python
# foo.py
x = 42

def grok(a):
    print(x)
```

아래를 보자.

```python
import foo

a = 10
foo.grok(a)
```

결과는 모듈은 독립적임을 보여준다.

```python
42
```

모듈이 임포트될 때, 파일의 끝에 도달할 때까지 *모듈의 모든 문장이 차례대로 실행된다*. 모듈 네임스페이스의 내용은 모두 *글로벌* 이름이며 실행 과정의 끝에 정의된다. 글로벌 스코프에서 작업(프린팅, 파일 생성 등)을 수행하는 스크립팅 문장이 있다면, 임포트할 때 수행되는 것을 볼 수 있을 것이다.

##### <span style="color:red">import as</span> 문

모듈을 임포하면서 모듈 이름에 별칭을 쓸 수 있다.

```python
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
```

##### <span style="color:red">from </span>모듈 import

```python
from math import sin, cos

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
```

### 임포트에 대한 설명

임포트를 어떤 방식으로 하든 모듈이 작동하는 방식은 변하지 않음

```python
import math
# vs
import math as m
# vs
from math import cos, sin
...
```

특히, `import`는 항상 파일 *전체*를 실행시키며 모듈은 환경과 여전히 분리된다.

<span style="color:red">import 모듈 as</span> 문은 로컬의 이름만 바꾼다. <span style="color:red">from math import cos, sin</span> 문은 여전히 math 모듈 전체를 적재한다. 이것을 수행하면 모듈에 있는 `cos`와 `sin`이 로컬 스페이스에 복사될 뿐이다

### 모듈 적재

각 모듈은 *단 한 번만* 적재 및 실행된다. *참고: 임포트를 여러 번 하더라도 이전에 적재한 모듈의 레퍼런스를 반환한다.*

`sys.modules`은 적재된 모듈 전체의 딕셔너리다.

```python
>>> import sys
>>> sys.modules.keys()
['copy_reg', '__main__', 'site', '__builtin__', 'encodings', 'encodings.encodings', 'posixpath', ...]
>>>
```

**주의:** 만약 모듈의 소스 코드를 변경한 후에 `import` 문을 수행하면 혼동이 생긴다. 모듈을 임포트하면 `sys.modules`에 캐시되므로, 임포트를 여러 번 수행하면 이전에 적재된 모듈이 반환되며, 모듈을 수정하더라도 반영되지 않는다. 수정한 모듈을 적재하는 가장 안전한 방법은 파이썬을 종료하고 다시 시작하는 것이다.

### 모듈 위치

파이썬은 모듈을 찾을 때 경로 리스트(sys.path)를 참고한다.

```python
>>> import sys
>>> sys.path
[
  '',
  '/usr/local/lib/python36/python36.zip',
  '/usr/local/lib/python36',
  ...
]
```

현재 작업 디렉터리가 가장 먼저 온다.

### 모듈 검색 경로

언급한 바와 같이, `sys.path`에는 검색 경로가 있다. 필요한 경우 수작업으로 변경할 수 있다.

환경 변수를 통해 경로를 추가할 수도 있다.

```python
% env PYTHONPATH=/project/foo/pyfiles python3
Python 3.6.0 (default, Feb 3 2017, 05:53:21)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)]
>>> import sys
>>> sys.path
['','/project/foo/pyfiles', ...]
```

일반적으로, 모듈 검색 경로를 수작업으로 조정할 필요는 없다. 하지만, 일반적이지 않은 위치에 있다든지 현재 작업 디렉터리에서 액세스할 준비가 되지 않은 파이썬 코드를 임포트할 일이 생기곤 한다.

### 연습 문제 3.11: 모듈 임포트

섹션 3에서 우리는 CSV 데이터 파일의 내용을 파싱하는 범용 함수 `parse_csv()`를 작성했다.

이제 그 함수를 다른 프로그램에서 사용하는 법을 알아보자. 먼저, 새로운 셸 창을 시작한다. 파일이 있는 폴더로 이동한다. 그 파일들을 임포트할 것이다.

파이썬 상호작용 모드를 시작한다.

```python
>>> import fileparse
>>> help(fileparse)
Help on module fileparse:

NAME
    fileparse

DESCRIPTION
    # fileparse.py
    #
    # Exercise 3.3
    # fileparse.py

FUNCTIONS
    parse_csv(filename, select=None, types=None, has_headers=False, delimiter=None, silence_errors=False)
        1.csv파일을 파싱해 레코드의 목록을 생성
        2.select - 보여주고자 하는 컬럼
        3.types - 형변환하고자 하는 타입을 리스트로 매개변수만들어서 던짐.
        4.has_header = False(헤더가 없음), True(헤더가 있음) - 예외처리
        5.ValueError에 대한 예외처리 추가
        6.ValueError시 예외처리 안하고 다음 루프로 진행하도록 처리(에러건은 무시하고 다음 건 처리)

FILE
    c:\dataanalysis\philosophy_datascience\02.python programming\practical-python\work\fileparse.py
```

```python
>>> import fileparse
>>> portfolio = fileparse.parse_csv("Data/portfolio.csv")
>>> porfolio
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'porfolio' is not defined
>>> portfolio
[('name', 'shares', 'price'), ('AA', '100', '32.20'), ('IBM', '50', '91.10'), ('CAT', '150', '83.44'), ('MSFT', '200', '51.23'), ('GE', '95', '40.37'), ('MSFT', '50', '65.10'), ('IBM', '100', '70.44')]

>>>pricelist = fileparse.parse_csv('Data/prices.csv',types=[str,float], has_headers=False)
>>> pricelist
[('AA', 9.22), ('AXP', 24.85), ('BA', 44.85), ('BAC', 11.27), ('C', 3.72), ('CAT', 35.46), ('CVX', 66.67), ('DD', 28.47), ('DIS', 24.22), ('GE', 13.48), ('GM', 0.75), ('HD', 23.16), ('HPQ', 34.35), ('IBM', 106.28), ('INTC', 15.72), ('JNJ', 55.16), ('JPM', 36.9), ('KFT', 26.11), ('KO', 49.16), ('MCD'
, 58.99), ('MMM', 57.1), ('MRK', 27.58), ('MSFT', 20.89), ('PFE', 15.19), ('PG', 51.94), ('T', 24.79), ('UTX', 52.61), ('VZ', 29.26), ('WMT', 49.74), ('XOM', 69.35)]
```

위와는 약간은 다른 방법으로..

```python
>>> from fileparse import parse_csv
>>> pricelist = fileparse.parse_csv('Data/prices.csv',types=[str,float], has_headers=False)
[('AA', 9.22), ('AXP', 24.85), ('BA', 44.85), ('BAC', 11.27), ('C', 3.72), ('CAT', 35.46), ('CVX', 66.67), ('DD', 28.47), ('DIS', 24.22), ('GE', 13.48), ('GM', 0.75), ('HD', 23.16), ('HPQ', 34.35), ('IBM', 106.28), ('INTC', 15.72), ('JNJ', 55.16), ('JPM', 36.9), ('KFT', 26.11), ('KO', 49.16), ('MCD'
, 58.99), ('MMM', 57.1), ('MRK', 27.58), ('MSFT', 20.89), ('PFE', 15.19), ('PG', 51.94), ('T', 24.79), ('UTX', 52.61), ('VZ', 29.26), ('WMT', 49.74), ('XOM', 69.35)]
>>>
```

### 연습문제 3.12 : report.py에서 fileparse.py를 임포트 해서 처리

```python
>>> import report
>>> report.portfolio_report('../../Work/Data/portfolio.csv', '../../Work/Data/prices.csv')
      Name     Shares      Price     Change
---------- ---------- ---------- ---------- 
        AA       100      9.22    -22.98
       IBM        50    106.28     15.18
       CAT       150     35.46    -47.98
      MSFT       200     20.89    -30.34
        GE        95     13.48    -26.89
      MSFT        50     20.89    -44.21
       IBM       100    106.28     35.84
```

### 연습문제 3.14 : 

```python
>>> import pcost
>>> Enter a filename : ../../Work/Data/portfolio.csv
Total cost :  44671.15
```


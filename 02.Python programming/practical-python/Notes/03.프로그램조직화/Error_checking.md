## 에러 확인하기

### 프로그램은 어떻게 실패하지?

파이썬은 함수에 전달되는 인자 타입 이나 값에 대해서 검사하거나 검증을 하지 않고 , 단지 함수내에서 구문에 적합한지를 확인할뿐이다.

그래서 실행시에는 에러를 내기때문에서 에러 핸들링이 중요하다.

```python
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hello', 'World')   # 'HelloWorld'
add('3', '4')           # '34'
```

아래와 같이 런타임시에 예외오류가 나온다.

```python
def add(x, y):
    return x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +:
'int' and 'str'
>>>
```

### 예외오류

예외오류는 사용자에게 호출한 프로그램에 문제가 있다는 신호를 주는 것으로 , 개발자가 데이터의 조건에 따라 예외 오류를 내기도 한다.

우리는 이것을 `예외오류를 낸다`다고 표현한다. 보통 `raise`를 사용.

```python
if name not in authorized:
    raise RuntimeError(f'{name} not authorized')
```

함수가 정상적으로 처리가 되기 위해서는 에러가 발생했을때 오류처리가 필요하다.

파이썬에서는 아래와 같이 오류에 대해서 예외처리를 한다.

```python
try:
    authentiate(name)
except RuntimeException as e:
    print(e)
```

### 오류 처리 

예외오류는 처음 만나는 `except`구문으로 전달된다.(propagate)

```python
def grok():
    ...
    raise RuntimeError('Whoa!')   # 예외 발생

def spam():
    grok()                        # 함수 호출

def bar():
    try:
       spam()
    except RuntimeError as e:     # 예외 캐취
        ...

def foo():
    try:
         bar()
    except RuntimeError as e:     # 예외가 여기까지 전달되지 못한다.
        ...

foo()
```

예외처리의 방법은 다음과 같다.

```python
def grok(): ...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # 예외를 여기서 잡고
        statements              # 처리
        statements
        ...

bar()
```

익셉션의 처리.

```python
def grok(): ...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Exception caught here
        statements
        statements
        ...
    statements                  # Resumes execution here
    statements                  # And continues here
    ...

bar()
```

### 내장된 예외오류

```python
ArithmeticError   - 산술연산 오류 
AssertionError
EnvironmentError
EOFError
ImportError
IndexError - 없는 배열의 인덱스를 참조하려고 시도할때.
KeyboardInterrupt
KeyError   - 없는 키값을 참조하는 경우 
MemoryError
NameError
ReferenceError  - 참조에러 
RuntimeError
SyntaxError
SystemError
TypeError   
ValueError    
```

## 예외오류 값

`exception`에는 오류 원인이 무엇인지 알수있는 값을 가지고 있음.

아래와 같이 에러를 발생시키고...

```python
raise RuntimeError("Invalid user name")
```

```python
try:
    ...
except RuntimeError as e:  # `e`값이 위에서 에러발생시 던지 에러내용을 포함하고있다.
    ...
```

```python
except RuntimeError as e:
    print("Error reason :", e)
```

### 여러개의 오류 처리

```python
try:
  ...
except LookupError as e:
  ...
except RuntimeError as e:
  ...
except IOError as e:
  ...
except KeyboardInterrupt as e:
  ...
```

```python
# 여러개의 오류를 그룹으로 처리
try:
  ...
except (IOError,LookupError,RuntimeError) as e:
  ...

```

### 모든 오류의 부모

```python
try:
    ...
except Exception as e:  # 모든 오류의 부모이기 때문에 에러시 모든 에러를 캐취가능
    ...
```

### 에러처리를 위한 바람직한 방법

```python
try:
    do_some()
except Exception as e:
    print('Error occurred : ', e)   # 바람직.
```

### 에러의 재발생시키기

호출자에게 에러처리를 위임하기 위해 `raise`를 사용하여 익셉션을 다시 발생시키기도 한다.

```python
try:
    do_something()
except Exception as e:
   	print("Error shoud be handled", e)
    raise 
```

### 바람직한 예외처리 방법

#### `finally`구문

```python
lock = lock()
lock.acquire()

try:
    ...
except Exception as e:
    print('Exception occurred : ', e)
finally:
    lock.release()  # 오류가 나더라도 해당 부분은 반드시 수행됨,연결해제,리소스잠금 해제 등등.
```

#### `with`구문 사용시.

`with`구문을 사용하면 자동적으로 메모리 혹은 연결 해제를 한다.

```python
lock = lock()

with lock.acquired():
    # 락 획득
# 끝나면 락이 자동적으로 해제됨
```

```python
with open(filename) as f:
    # 코드 
# 파일 닫음    
```

### 연습문제 3.8: 파라미터의 sanity체크를 통한 예외발생

`fileparse.py`를 `select - 보여주고자 하는 컬럼` 인자가 있고, `has_headers=False`로 넘어오는 경우에 예외를 발생시켜 프로그램을 정상적으로 종료시키도록 수정해보자.

```python
# fileparse.py
import csv

def parse_csv(filename,select=None, types=None, has_headers=False, delimiter = None):
    '''
    1.csv파일을 파싱해 레코드의 목록을 생성
    2.select - 보여주고자 하는 컬럼
    3.types - 형변환하고자 하는 타입을 리스트로 매개변수만들어서 던짐.
    4.has_header = False(헤더가 없음), True(헤더가 있음)
    '''
    if select and not has_headers:
        raise RuntimeError("헤더값이 잘못넘어왔네요.")
    with open(filename) as f:
        if delimiter:
            rows = csv.reader(f, delimiter=delimiter)
        else:
            rows = csv.reader(f)
        
        headers = next(row) if has_headers else []
        
        # 보여주고자 하는 컬럼정보가 있으면 
        if select:
            indices = [headers.index(name) for name in select]
            headers = select
        else:  # 없으면.
            indices = []        
        
        records = []
        for row in rows:
            try:                
                if not row:
                    continue  # 다음 루프 진행

                if indices:  # 존재하면 
                    row = [row[idx] for idx in indices]
                if types: #존재하면
                    row = [fnc(val)for fnc,val in zip(types, row)]

                # 헤더가 있는 경우만 딕셔너리로 리턴해야 되니까.    
                if has_headers:
                    record = dict(zip(headers, row))
                else:  # 헤더가 없는 경우는 튜플로 리턴
                    record = tuple(row)
                records.append(record)
            except ValueError:
                pass
        return records
```

### 연습문제 3.9 : ValueError에 대한 오류 처리

```python
>>> portfolio = parse_csv('../../Work/Data/missing.csv', types=[str, int, float])
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
>>> portfolio
[{'price': 32.2, 'name': 'AA', 'shares': 100}, {'price': 91.1, 'name': 'IBM', 'shares': 50}, {'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 40.37, 'name': 'GE', 'shares': 95}, {'price': 65.1, 'name': 'MSFT', 'shares': 50}]
>>>
```

위와 같이 오류에 대한 처리를 하고 보여주어야 한다면?

```python
# fileparse.py
import csv

def parse_csv(filename,select=None, types=None, has_headers=False, delimiter = None):
    '''
    1.csv파일을 파싱해 레코드의 목록을 생성
    2.select - 보여주고자 하는 컬럼
    3.types - 형변환하고자 하는 타입을 리스트로 매개변수만들어서 던짐.
    4.has_header = False(헤더가 없음), True(헤더가 있음)
    5.ValueError대한 오류 처리 및 오류내용 보여주기 추가.
    '''
    if select and not has_headers:
        raise RuntimeError("헤더값이 잘못넘어왔네요.")
    with open(filename) as f:
        if delimiter:
            rows = csv.reader(f, delimiter=delimiter)
        else:
            rows = csv.reader(f)
        
        headers = next(row) if has_headers else []
        
        # 보여주고자 하는 컬럼정보가 있으면 
        if select:
            indices = [headers.index(name) for name in select]
            headers = select
        else:  # 없으면.
            indices = []        
        
        records = []
        idx = 1
        for row in rows:
            try:                
                if not row:
                    continue  # 다음 루프 진행

                if indices:  # 존재하면 
                    row = [row[idx] for idx in indices]
                if types: #존재하면
                    row = [fnc(val)for fnc,val in zip(types, row)]

                # 헤더가 있는 경우만 딕셔너리로 리턴해야 되니까.    
                if has_headers:
                    record = dict(zip(headers, row))
                else:  # 헤더가 없는 경우는 튜플로 리턴
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                print("Row %d : Couldn't convert %r " %(idx, row))  
                print('Row %d : Reason %s' %(idx, e))
        return records
```

### 연습문제 3.10 :예외를 무시하고 다음 반복으로 넘어가도록 처리

```python
# fileparse.py
import csv

def parse_csv(filename,select=None, types=None, has_headers=False, delimiter = None, silence_errors=False):
    '''
    1.csv파일을 파싱해 레코드의 목록을 생성
    2.select - 보여주고자 하는 컬럼
    3.types - 형변환하고자 하는 타입을 리스트로 매개변수만들어서 던짐.
    4.has_header = False(헤더가 없음), True(헤더가 있음) - 예외처리
    5.ValueError에 대한 예외처리 추가
    6.silence_errors 파라미터 - ValueError시 예외처리 안하고 다음 루프로 진행하도록 처리(에러건은 무시하고 다음 건 처리)
    '''
    if (select and not has_headers):
        raise RuntimeError("헤더값이 잘못넘어왔네요.")
        
    with open(filename) as f:
        if delimiter:
            rows = csv.reader(f, delimiter=delimiter)
        else:
            rows = csv.reader(f)
        
        headers = next(row) if has_headers else []
        
        # 보여주고자 하는 컬럼정보가 있으면 
        if select:
            indices = [headers.index(name) for name in select]
            headers = select
        else:  # 없으면.
            indices = []        
        
        records = []
        idx = 1
        for row in rows:
            try:                
                if not row:
                    continue  # 다음 루프 진행

                if indices:  # 존재하면 
                    row = [row[idx] for idx in indices]
                if types: #존재하면
                    row = [fnc(val)for fnc,val in zip(types, row)]

                # 헤더가 있는 경우만 딕셔너리로 리턴해야 되니까.    
                if has_headers:
                    record = dict(zip(headers, row))
                else:  # 헤더가 없는 경우는 튜플로 리턴
                    record = tuple(row)
                records.append(record)
                idx += 1
            except ValueError as e:
                if silence_errors:
                    idx += 1
                    continue
                else:
                    print("Row %d : Couldn't convert %r " %(idx, row))
                    print('Row %d : Reason %s' %(idx, e))
                    idx += 1
        return records
```

그럼 아래와 같이 에러가 없이 다음건을 처리한다.

 ```python
# 수행하면 익셉션처리가 무시하고 바로 다음 루프를 처리
>>>portfolio = parse_csv('../../Work/Data/missing.csv', types=[str,int,float], silence_errors=True)
>>>portfolio
[('AA', 100, 32.2),
 ('IBM', 50, 91.1),
 ('CAT', 150, 83.44),
 ('GE', 95, 40.37),
 ('MSFT', 50, 65.1)]
 ```

**에러처리는 위의 처럼 무시하고 넘어가지 말고, Exception을 처리함으로써 사용자에게 어떤 대응조치를 취할수있도록 처리해야 됨을 유념하자.**


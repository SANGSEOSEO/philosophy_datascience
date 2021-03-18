# 함수의 작동

------

이번 장에서는 함수를 호출시에는 호출규약(calling conventions) 과 스코핑 규칙들을 알아보고자 한다.

## 함수 호출

```python
def read_prices(filename, debug):
    ...
```

위치인자(positional arguments)를 사용해 호출 할 수도 있다.

```
prices = read_prices('prices.csv', True)
```

혹은 키워드 인자(keyword arguments)를 이용해 호출 할수도 있다.

```python
prices = read_prices(filename='prices.csv', debug=True)
```

## 기본인자

호출시 인자를 선택사항으로 두고 싶을때는 , 디폴트값을 주는 것이 좋다.

```python
def read_prices(filename, debug=False):
    ...
```

함수 정의시, 기본값이 지정되면 함수 호출시에 값은 선택적이다.

```python
d = read_prices('prices.csv')
d = read_prices('prices.csv', True)
```

* 주의 : 파라미터가 디폴트값이 지정되어 있는 파라미터가 있는 경우는 반드시 해당 인자는 맨 뒤에 위치해야 한다.

```python
parse_data(data, False, True) # ?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```

키워드 인자를 사용하는 것이 가독성이 높다.

### 설계 모범사례

함수인자는 짧되, 의미있는 이름이어야 가독성에 좋다.

```python
d = read_prices('prices.csv', debug=True)
```

### 반환 값

`return`문은 값을 반환한다.

```python
def square(x):
    return x *x
```

`return`문이 없거나 반환값이 없으면 `None`을 리턴한다.

```python
def bar(x):
    statements
    return
def bar(x):
    statements
    return

a = bar(4)      # a = None

# OR
def foo(x):
    statements  # No `return`

b = foo(4)      # b = None
```

### 여러개의 값을 반환

함수는 한 개의 값만 리턴 가능하지만, 리턴 타입을 튜플로 하게되면 여러개의 값을 튜플형태로 리턴이 가능하다.

```python
def divide(a,b):
    q = a // b      # 몫
    r = a % b       # 나머지
    return q, r     # 튜플을 반환
```

사용 예:

```python
x, y = divide(37,5) # x = 7, y = 2

x = divide(37, 5)   # x = (7, 2)
```

### 변수 스코프

프로그램은 변수에 값을 할당한다.

```pyton
x = value # 글로벌 변수

def foo():
    y = value # 로컬 변수
```

함수 바깥에 선언된 변수를 `global`변수이고, 함수 내부에 선언된 변수는 `local`변수이다.

### 로컬변수

함수내에 할당된 변수는 private이다.

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        try:
            fields = line.split(',')
            s = (fields[0].replace('"', ''), int(fields[1]), float(fields[2]))
            portfolio.append(s)
        except ValueError:
            pass
    return portfolio   
```

실행결과는 아래와 같다.

없는 변수를 참조하는 경우는 에러가 아래와 같이 나겠지.

```python
>>data = read_portfolio('../../Work/Data/portfolio.csv')
>>data
[('AA', 100, 32.2),
 ('IBM', 50, 91.1),
 ('CAT', 150, 83.44),
 ('MSFT', 200, 51.23),
 ('GE', 95, 40.37),
 ('MSFT', 50, 65.1),
 ('IBM', 100, 70.44)]
>>fields
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-20-8ece27c95e41> in <module>
----> 1 fileds

NameError: name 'fileds' is not defined

```

### 전역변수(global variable)

함수는 자유롭게 전역변수를 참조할수 있다.

```python
name = 'Dave'

def greeting():
    print('Hello', name)  # Using `name` global variable
```

하지만 함수는 전역변수의 값을 바꿀수있을까?

```python
def spam():
    name = 'Spam'
```

```python
>>spam()  # 에러는 안나지만 값은 변경되지 않음.
>>name
'Dave'
```

**함수내에서 선언되고 할당되는 모든 변수의 스콥은 로컬이다.**

만약, 글로벌 변수를 변경하고 싶다면 아래와 같은 변경해야 한다.

```python
def spam():
    global name 
    name = 'Spam'  # change the global name above
```

```python
>>spam()
>>display(name)
'Spam'
```

**하지만 가능하다면 `global`변수를 사용하지 않도록 하라.** 

### 인자전달

변경 가능한 자료형(list, dict)을 인자로 전달하는 경우에, 함수내에서 수정을 하면 전달하는 인자가 변경됨을 유의하라.

```python
def foo(items):
    items.append(42)    # 입력 객체를 수정

a = [1, 2, 3]
foo(a)
print(a) 
>> [1, 2, 3, 42]
```

### 재할당 vs 수정

변수를 수정하는 것과 변수명을 재할당하는 것의 미묘한 차이를 이해해야 한다.

```python
def foo(items):
    items.append(42)    # 입력 객체를 수정

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# VS
def bar(items):
    items = [4,5,6]    # 다른 객체를 가리키도록 로컬 `items` 변수를 변경

b = [1, 2, 3]
bar(b)
print(b)                # [1, 2, 3]
```

**Note : 변수 할당은 메모리를 절대 덮어쓰지 않는다. 이름은 새 값에 바운드된다.**

### 연습문제 3.3 CSV 파일 읽기 

```python
# fileparse.py
import csv

def parse_csv(filename):
    '''
    csv파일을 파싱해 레코드의 목록을 생성
    '''
    with opne(filename) as f:
        rows = csv.reader(f)
        
        # 헤더를 읽음
        headers = next(rows)
        records = []
        for row in rows:
            if not row:
                continue  # 다음 루프 진행
            record = dict(zip(headers, row))
            records.append(record)
        
    return records
```

아래와 같이 수행하면...

```python
data = parse_csv('../../Work/Data/portfolio.csv')
data
>>>
[{'name': 'AA', 'shares': '100', 'price': '32.20'},
 {'name': 'IBM', 'shares': '50', 'price': '91.10'},
 {'name': 'CAT', 'shares': '150', 'price': '83.44'},
 {'name': 'MSFT', 'shares': '200', 'price': '51.23'},
 {'name': 'GE', 'shares': '95', 'price': '40.37'},
 {'name': 'MSFT', 'shares': '50', 'price': '65.10'},
 {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

### 연습 문제 3.4: 컬럼 선택기 구축하기

보고싶은 컬럼만 보고 싶다고 한다면 What if I do?

```python
# fileparse.py
import csv

def parse_csv(filename,select=None):
    '''
    csv파일을 파싱해 레코드의 목록을 생성
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        
        # 헤더를 읽음
        headers = next(rows)
        
        # 보여주고자 하는 컬럼정보가 있으면 
        if select:
            indices = [headers.index(name) for name in select]
            headers = select
        else:  # 없으면.
            indices = []        
        
        records = []
        for row in rows:
            if not row:
                continue  # 다음 루프 진행
            
            if indices:  # 존재하면 
                row = [row[idx] for idx in indices]
                
            record = dict(zip(headers, row))
            records.append(record)
        
    return records
```

위와 같이 생성하기 전에 REPL(Read Eval Print Loop)를 먼저 해보았다.

```python
>>>headers = ['name', 'date', 'time', 'shares', 'price']
>>>select = ['name', 'shares']
>>>row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
```

이렇다고 할때, 보여주고하는 컬럼(select)의 `이름`을 가지고 `headers`정보에서 `headers.index(컬럼이름)`으로 찾을 수있다.

```python
>>>indices = headers.index('name')  # 이름으로 인덱스를 알수있다.
>>>row[indices]
'AA'
```

그럼, 위의 함수를 수행해보자.

```pthon
>>>filename = '../../Work/Data/portfolio.csv'
>>>select = ['name', 'shares']
>>>data = parse_csv(filename, select)
>>>data
```

결과는 아래와 같다.

```python
>>>data
[{'name': 'AA', 'shares': '100'},
 {'name': 'IBM', 'shares': '50'},
 {'name': 'CAT', 'shares': '150'},
 {'name': 'MSFT', 'shares': '200'},
 {'name': 'GE', 'shares': '95'},
 {'name': 'MSFT', 'shares': '50'},
 {'name': 'IBM', 'shares': '100'}]
```

### 연습문제 3-5 : 컬럼의 형변환

```python
# fileparse.py
import csv

def parse_csv(filename,select=None, types=None):
    '''
    1.csv파일을 파싱해 레코드의 목록을 생성
    2.select - 보여주고자 하는 컬럼
    3.types - 형변환하고자 하는 타입을 리스트로 매개변수만들어서 던짐.
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        
        # 헤더를 읽음
        headers = next(rows)
        
        # 보여주고자 하는 컬럼정보가 있으면 
        if select:
            indices = [headers.index(name) for name in select]
            headers = select
        else:  # 없으면.
            indices = []        
        
        records = []
        for row in rows:
            if not row:
                continue  # 다음 루프 진행
            
            if indices:  # 존재하면 
                row = [row[idx] for idx in indices]
            if types: #존재하면
                row = [fnc(val)for fnc,val in zip(types, row)]
            
            record = dict(zip(headers, row))
            records.append(record)
        return records
```

수행해보면?

```python
>>>filename = '../../Work/Data/portfolio.csv'
>>>select = ['name', 'shares', 'price']
>>>types  = [str, int, float]
>>>stock = parse_csv(filename, select, types)
>>>stock
[{'name': 'AA', 'shares': 100, 'price': 32.2},
 {'name': 'IBM', 'shares': 50, 'price': 91.1},
 {'name': 'CAT', 'shares': 150, 'price': 83.44},
 {'name': 'MSFT', 'shares': 200, 'price': 51.23},
 {'name': 'GE', 'shares': 95, 'price': 40.37},
 {'name': 'MSFT', 'shares': 50, 'price': 65.1},
 {'name': 'IBM', 'shares': 100, 'price': 70.44}]
```

### 연습문제 3.6: 헤더가 없는 CSV

```python
>>> prices = parse_csv('Data/prices.csv', types=[str,float], has_headers=False)
>>> prices
[('AA', 9.22), ('AXP', 24.85), ('BA', 44.85), ('BAC', 11.27), ('C', 3.72), ('CAT', 35.46), ('CVX', 66.67), ('DD', 28.47), ('DIS', 24.22), ('GE', 13.48), ('GM', 0.75), ('HD', 23.16), ('HPQ', 34.35), ('IBM', 106.28), ('INTC', 15.72), ('JNJ', 55.16), ('JPM', 36.9), ('KFT', 26.11), ('KO', 49.16), ('MCD', 58.99), ('MMM', 57.1), ('MRK', 27.58), ('MSFT', 20.89), ('PFE', 15.19), ('PG', 51.94), ('T', 24.79), ('UTX', 52.61), ('VZ', 29.26), ('WMT', 49.74), ('XOM', 69.35)]
>>>
```

**CSV의 첫번째 라인을 헤더로 인식하면 안되고, 두번째로 리턴타입이 딕셔너리가 아닌 튜풀로 리턴해야 줘야 한다.조건에 따라 달라져야 함.**

```PYTHON
# fileparse.py
import csv

def parse_csv(filename,select=None, types=None, has_headers=False):
    '''
    1.csv파일을 파싱해 레코드의 목록을 생성
    2.select - 보여주고자 하는 컬럼
    3.types - 형변환하고자 하는 타입을 리스트로 매개변수만들어서 던짐.
    4.has_header = False(헤더가 없음), True(헤더가 있음)
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        
        if has_headers:
            # 헤더를 읽음
        	headers = next(rows)
        
        # 보여주고자 하는 컬럼정보가 있으면 
        if select:
            indices = [headers.index(name) for name in select]
            headers = select
        else:  # 없으면.
            indices = []        
        
        records = []
        for row in rows:
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
        return records
```

**수행**

```python
>>>prices = parse_csv('../../Work/Data/prices.csv', types=[str,float], has_headers=False)
>>>prices
[('AA', 9.22),
 ('AXP', 24.85),
 ('BA', 44.85),
 ('BAC', 11.27),
 ('C', 3.72),
 ('CAT', 35.46),
 ('CVX', 66.67),
 ('DD', 28.47),
 ('DIS', 24.22),
 ('GE', 13.48),
 ('GM', 0.75),
 ('HD', 23.16),
 ('HPQ', 34.35),
 ('IBM', 106.28),
 ('INTC', 15.72),
 ('JNJ', 55.16),
 ('JPM', 36.9),
 ('KFT', 26.11),
 ('KO', 49.16),
 ('MCD', 58.99),
 ('MMM', 57.1),
 ('MRK', 27.58),
 ('MSFT', 20.89),
 ('PFE', 15.19),
 ('PG', 51.94),
 ('T', 24.79),
 ('UTX', 52.61),
 ('VZ', 29.26),
 ('WMT', 49.74),
 ('XOM', 69.35)]
```

### 연습문제 3.7: 다른 컬럼구분자(column delimiter)

살다보면 , 콤마가 아닌 다른 형태의 컬럼 구분자를 보게 된다.

```Data/portfolio.dat```를 보면 구분자가 `스패이스`로 이루어짐을 볼 수 있다.

```python
name shares price
"AA" 100 32.20
"IBM" 50 91.10
"CAT" 150 83.44
"MSFT" 200 51.23
"GE" 95 40.37
"MSFT" 50 65.10
"IBM" 100 70.44
```

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

수행하면?

```python
>>>portfolio = parse_csv('../../Work/Data/portfolio.dat', types=[str, int, float], delimiter=' ')
>>>portfolio
[('AA', 100, 32.2),
 ('IBM', 50, 91.1),
 ('CAT', 150, 83.44),
 ('MSFT', 200, 51.23),
 ('GE', 95, 40.37),
 ('MSFT', 50, 65.1),
 ('IBM', 100, 70.44)]
```


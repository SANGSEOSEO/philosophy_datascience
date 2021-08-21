

## 01.파이썬과 유니코드

컴퓨터는 0과 1이라는 값만을 인식할 수 있는 기계장치이다. 컴퓨터가 문자를 인식할 수 있게 하려면 어떻게 해야 할까? 과거부터 지금까지 사용하는 유일한 방법은 다음과 비슷한 방법의 문자셋을 만드는 것이다.

각 나라마다 매핑해야 하는 문자셋이 다르다 보니 이 기종 컴퓨터간의 문제없이 데이터를 주고 받기 위해서 미국에서 최초로 문자셋 표준인 **아스키(ASCII)**가 탄생하게 된다. 

아스키라는 문자셋 규칙을 정하고 이 규칙대로만 문자를 만들면 이 기종 컴퓨터간에도 문제없이 데이터를 주고 받을 수 있게 되는 것이다. 

아스키는 처리할 수 있는 문자의 갯수가 **127개** 였는데 이것은 영어권 국가들에서 사용하는 영문자, 숫자등을 처리하기 위해서는 부족함이 없었다. 하지만 곧 비 영어권 국가들에서도 자신들의 문자를 컴퓨터로 표현해야 하는 요구들이 발생하게 되었다. 

아스키는 127개의 문자만을 다룰 수 있기 때문에 아스키를 사용할 수는 없는 노릇이었다. 

그래서 곧 서유럽 문자셋인 **ISO8859**가 등장하게 되고 한국에서는 **KSC5601**과 같은 문자셋들이 등장하게 된다.

이렇게 나라별로 문자셋이 만들어지고 또 한 나라에서도 여러개의 문자셋이 표준이 되기 위한 치열한 싸움을 벌이기도 하며 문자를 처리하기 위한 방법은 점점 더 계속 복잡해져만 갔다.

가장 결정적인 문제는 하나의 문서에 여러나라의 언어를 동시에 표현할 수 있는 방법이 없었다는 점이다.

이런 문제를 해결하기 위해서 등장한 것이 바로 **유니코드(Unicode)**이다. 

유니코드는 모든 나라의 문자를 다 포함하게끔 넉넉하게 설계되었고 곧 세계적인 표준으로 자리잡게 되었다. 이 유니코드라는 규칙을 사용하게 되면 서로 다른 문자셋으로 고생할 일이 이제 없어지게 된 것이다.

```
1. 인코딩
2. 디코딩
3. 입출력과 인코딩
4. 소스코드 인코딩
```

#### 인코딩 (encoding)

```python
>>> a = "Life is too short"
>>> type(a)
<class 'str'>
```

파이썬 3부터는 모든 문자열은 유니코드 문자열이다. 유니코드 문자열을 인코딩없이 그대로 파일에 적거나 다른 시스템으로 전송할 수 없다.왜냐하면 유니코드는 단순히 문자셋의 규칙이기 때문이다.

파일에 적거나 다른 시스템으로 유니코드 문자열을 전송하기 위해서는 바이트로 변환해야 한다.이렇게 유니코드 문자열을 바이트로 변환하는 것을 인코딩이라고 한다.

따라서 파일을 읽거나 바이트 문자열을 수신받을 때에는 해당 바이트가 어떤 방식의 인코딩을 사용했는지는 필수적으로 미리 알고 있어야만 디코딩이 가능하다.

유니코드 문자열을 바이트 문자열로 바꾸는 방법

```
>>> a = 'Life is too short'
>>> b = a.encode('utf-8')
>>> b
b'Life is too short'
>>> type(b)
<class 'bytes'>
```

유니코드 문자열을 바이트 문자열로 만들 때에는 위 예처럼 인코딩 방식을 파라미터로 넘겨 주어야 한다. 

파라미터를 생략하면 디폴트 값인 utf-8로 동작한다.

```
>>> a = "한글"
>>> a.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```

`한글`이라는 유니코드 문자열을 아스키 방식으로 인코딩시도했는데 에러가 난 케이스를 보면 ascii방식으로는 한글을 표현 할 수 가 없어 에러가 난 케이스.

`euc-kr`로 인코딩해서 표현 가능함을 확인해보자

```
>>> a.encode('euc-kr')
b'\xc7\xd1\xb1\xdb'
>>> b = a.encode('utf-8')
b'\xed\x95\x9c\xea\xb8\x80'
>>>
```

#### 디코딩 (decoding)

이번에는 반대로 인코딩된 바이트 문자열을 유니코드 문자열로 변환할 수 있는 디코딩에 대해서 알아보자. 다음 예제처럼 euc-kr로 인코딩된 바이트 문자열은 euc-kr로만 디코딩을 해야 한다.

```
>>> a = "한글"
>>> b = a.encode("euc-kr")
>>> b.decode('euc-kr')
'한글'
```

잘못된 방식으로 디코딩을 할 경우 발생하는 오류

```
>>> b.decode('utf-8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc7 in position 0: invalid continuation byte
```



#### 입출력과 인코딩

인코딩 관련해서 개발자들이 가장 고생하는 부분은 바로 데이터의 입출력 관련해서이다. 이것 역시 문자열과 인코딩에 대한 개념만 확실히 이해하면 어렵지 않지만 이것들에 대한 이해 없이 무작정 인코딩, 디코딩을 사용하면 다중 인코딩되거나 다중 디코딩되면서 문자열이 꼬여 버리는 불상사가 발생하기도 한다.

파일을 읽거나 네트워크를 통해 데이터를 입력받을 때 추천하는 방법은 다음과 같다.

1. 입력으로 받은 바이트 문자열을 가능한 한 가장 빨리 유니코드 문자열로 디코딩 할 것.
2. 변환된 유니코드 문자열로만 함수나 클래스등에서 사용할 것.
3. 입력에 대한 결과를 전송하는 마지막 부분에서만 유니코드 문자열을 바이트 문자열로 인코딩해서 리턴할것

위와 같은 규칙을 준수한다면 인코딩 관련해서 큰 어려움이 없을 것이다.

다음은 euc-kr 방식으로 작성되어진 파일을 읽고 변경하여 저장하는 예제이다.

```
# 1. euc-kr로 작성된 파일 읽기
with open('euc_kr.txt', encoding='euc-kr') as f:
    data = f.read()  # 유니코드 문자열 

# 2. unicode 문자열로 프로그램 수행하기
data = data + "\n" + "추가 문자열"

# 3. euc-kr로 수정된 문자열 저장하기
with open('euc_kr.txt', encoding='euc-kr', mode='w') as f:
    f.write(data)
```

파일을 읽는 open 함수에는 encoding을 지정하여 파일을 읽을 수 있는 기능이 있다. 이 때 읽어들인 문자열은 유니코드 문자열이 된다. 마찬가지로 파일을 작성할 때도 encoding을 지정하여 파일을 작성할 수 있다. 만약 encoding항목을 생략하면 디폴트로 utf-8이 지정된다.

#### 소스코드 인코딩

파이썬 셸이 아닌 에디터로 파이썬 코딩을 할 경우 소스 코드의 인코딩은 매우 중요하다. 

소스 코드의 인코딩이란 소스 코드 파일이 현재 어떤 방식으로 인코딩되었지를 의미한다.

우리가 위 예제에서 알아보았듯이 파일은 utf-8 인코딩으로 저장할 수도 있고 euc-kr로 저장할 수도 있었다. 

소스 코드도 파일이므로 인코딩 타입이 반드시 존재한다. 

파이썬은 소스코드의 인코딩을 명시하기 위해 소스 코드 제일 상단에 다음과 같은 문장을 넣어 주어야 한다.

```
# -*- coding: utf-8 -*-
```

만약 소스코드가 utf-8로 인코딩된 파일이라면 위와 같이 작성하면 되고 euc-kr로 인코딩된 경우라면 다음과 같이 작성해야 한다.

> 파이썬 3.0 부터는 utf-8이 디폴트이므로 utf-8로 인코딩된 소스 코드인 경우 위 문장을 생략 해도 된다.

```
# -*- coding: euc-kr -*-
```

만약 소스코드는 euc-kr로 인코딩되었는데 파일상단에는 utf-8로 명시되어져 있다면 문자열 처리하는 부분에서 인코딩 관련한 오류가 발생할 것이다.

## 02 클로저와 데코레이터

데코레이터를 이해하기 위해서는 먼저 클로저에 대한 이해가 필요하다. 클로저에 대해서 먼저 알아본 후 데코레이터에 대해서 알아보자.

### 클로저

클로저는 간단히 말해 함수 내에 내부 함수(inner function)를 구현하고 그 내부 함수를 리턴하는 함수를 말한다. 이 때 외부 함수는 자신이 가지고 있는 변수값 등을 내부 함수에 전달하여 실행될 수 있게 한다.(**자바스크립트 개념의 클로저와 유사**)

알쏭 달쏭한 설명이지만 예제를 보면 쉽게 이해할 수 있다.

어떤 수에 항상 3을 곱해서 리턴해 주는 함수를 생각해 보자. 아마도 다음과 같은 함수를 만들 수 있을 것이다.

```
>>> def mul3(n):
...    return n * 3
```

이번에는 5를 곱해서 리턴해주는 함수를 만든다.

```
>>> def mul5(n):
...    return n * 5
```

하지만, 필요에 따라 이렇게 함수를 만드는것은 비효율적이다.

그래서 우리는 아래와 같이 클래스를 만들게 된다

```
# -*- coding: utf-8 -*-
"""
class example
"""
class Mul:
    def __init__(self, m):
        self.m = m
        
    def mul(self, n):
        return self.m * n

if __name__ =="__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)    
    
    print(mul3.mul((10)))
    print(mul5.mul(10))
```

결과는 다음과 같다

```
30
50
```

<span style="color:red">`__call__`</span>메소드를 이용해 좀 더 개선해보자. <span style="color:red">`__call__`함수</span>는 Mul클래스로 만들어진 객체에 인수를 전달하여 바로 호출 할 수 있게 해주는 메소드.

<span style="color:red">`__call__`</span>메소드를 이용하면 아래 mul3객체를 mul3(10)객체 처럼 쓸 수 있다.

```
# -*- coding: utf-8 -*-
"""
class example
"""

class Mul:
    def __init__(self, m):
        self.m = m
        
    #def mul(self, n):
     #   return self.m * n
    
    def __call__(self, n):
        return self.m * n
    


if __name__ =="__main__":
    mul3 = Mul(3)  #30출력
    mul5 = Mul(5)  # 50출력   
    #호출방법이 달라짐에 유의
    print(mul3((10)))
    print(mul5(10))
```

결과는 위의 것과 동일하다.

다음과 같은 방법으로도 시도해보면.

```
def mul(m):
    def wrapper(n):
        return m * n
    return wrapper


if __name__ == "__main__":
    mul3 = mul(3)
    mul5 = mul(5)

    print(mul3(10))  # 30 출력
    print(mul5(10))  # 50 출력
```

바깥 함수(mul)안에 안쪽 함수(wrapper)가 구현되어 있다. 그리고 바깥 함수는 안쪽 함수 wrapper를 리턴한다. 

함수에서 함수를 리턴하는 것이 생소할 수 있겠지만 파이썬은 이것이 가능하다.

재밌는 사실은 mul 함수에서 wrapper 함수를 리턴할 때 mul 함수 호출시 인수로 받은 m의 값이 wrapper 함수에 저장되어 리턴된다는 점이다. 이것은 마치 클래스가 특정한 값을 설정하여 객체를 만들어 내는 과정과 매우 흡사하다.

이러한 mul과 같은 함수를 파이썬에서는 **클로저(Closure)**라고 한다.

### 데코레이터

다음은 "함수가 실행됩니다" 라는 문자열을 출력하는 myfunc 함수이다.

```
def myfunc():
    print("함수가 실행됩니다.")
```

그런데 이 함수의 수행시간을 측정해야 한다면 어떻게 해야 할까?

함수의 수행시간은 함수가 시작하는 순간의 시간과 함수가 종료되는 순간의 시간 차이를 구하면 알 수 있다. 따라서 다음과 같이 코드를 수정하면 함수의 총 수행시간을 측정할 수 있다.

```
import time

def myFunc():
    
    sTime = time.time()
    print("함수가 실행됩니다.")
    eTime = time.time()
    
    print("총 수행 시간 : {}".format(eTime - sTime))
    
if __name__ == "__main__":
    myFunc()
```

실행결과는 다음과 같다.

```
runcell(0, 'C:/Users/cello/.spyder-py3/temp.py')
함수가 실행됩니다.
총 수행 시간 : 0.0
```

하지만 수행시간을 측정해야 하는 함수가 무수히 많다면 어떻게 해야 하지?

그 모든 함수를 다 수정해야 하나?

```
import time

def elapsed(origianl_func): 
    """
    Parameters
    ----------
    origianl_func : myfunc
        수행시간 측정
    Returns
    -------
    wrapper.

    """
    def wrapper():
        """
        장식된 함수를 수행한 결과를 리턴
        """
        start  = time.time()
        result = origianl_func() # 기존 함수 수행
        end = time.time()
        print("함수 수행시간 : %f 초" %(end - start)) # 기존 함수의 수행시간 측정
        return result  # 기존 함수의 수행결과를 리턴
    return wrapper        


def myfunc():
    print("함수가 실행됩니다.")
    
    
decorated_myfunc = elapsed(myfunc)  # 장식된 함수를 호출하면 
decorated_myfunc()
```

elapsed 함수로 클로저를 만들었다. elapsed 함수는 함수를 인수로 받는다. 파이썬은 함수도 객체이기 때문에 함수 자체를 인수로 전달하는 것이 가능하다.

이제 `decorated_myfunc = elapsed(myfunc)`로 생성된 decorated_myfunc를 `decorated_myfunc()` 처럼 실행하면 실제로는 elapsed 내부의 wrapper 함수가 실행되고 wrapper 함수는 전달 받은 myfunc 함수를 수행하고 수행시간도 함께 출력할 것이다.

클로저를 이용하면 기존 함수에 뭔가 추가적인 부가 기능을 덧붙이기가 아주 편리하다. 이렇게 기존 함수의 변경 없이 추가적인 기능을 덧붙일 수 있도록 해 주는 elapsed 함수와 같은 클로저를 **데코레이터(Decorator)**라고 한다.

> 영어 단어 'decorate'는 "장식하다" 라는 뜻이다. 그런 의미에서 데코레이터는 함수를 꾸며주는 함수라고 생각해도 좋을 것이다.

수행 결과는 다음과 같다.

```
함수가 실행됩니다.
함수 수행시간 : 0.000000 초
```

파이썬 데코레이터는 다음처럼 `@`를 이용한 어노테이션을 사용할수도 있다.

```
import time

def elapsed(origianl_func): 
    """
    Parameters
    ----------
    origianl_func : function
        수행시간 측정
    Returns
    -------
    wrapper.

    """
    def wrapper():
        start  = time.time()
        result = origianl_func() # 기존 함수 수행
        end = time.time()
        print("함수 수행시간 : %f 초" %(end - start)) # 기존 함수의 수행시간 측정
        return result  # 기존 함수의 수행결과를 리턴
    return wrapper        

@elapsed
def myfunc():
    print("함수가 실행됩니다.")
    

# @elapsed 어노테이션으로 인해 더이상 필요하지 않다.    
# decorated_myfunc = elapsed(myfunc)
# decorated_myfunc()

myfunc()
```

수행결과는 아래와 같다.

```
함수가 실행됩니다.
함수 수행시간 : 0.000000 초
```

그렇다면 myfunc함수를 다음과 같이 수행해보자.

```
import time

def elapsed(origianl_func): 
    """
    Parameters
    ----------
    origianl_func : function
        수행시간 측정
    Returns
    -------
    wrapper.

    """
    def wrapper():
        start  = time.time()
        result = origianl_func() # 기존 함수 수행
        end = time.time()
        print("함수 수행시간 : %f 초" %(end - start)) # 기존 함수의 수행시간 측정
        return result  # 기존 함수의 수행결과를 리턴
    return wrapper        

@elapsed
def myfunc(msg):
    print("'%s'를 출력합니다." %msg)  


myfunc("You need python")
```

원래 함수가 인자를 받도록 수정하고, 수행해보면 아래와 같은 오류가 난다.

```
line 27, in <module>
    myfunc("You need python")

TypeError: wrapper() takes 0 positional arguments but 1 was given
```

오류의 원인은 myfunc 함수는 입력인수를 필요로 하지만 elapsed 함수 내의 wrapper 함수는 전달받은 myfunc 함수를 입력인수 없이 호출하기 때문이다.

데코레이터 함수는 기존 함수의 입력 인수에 상관없이 동작하도록 만들어야 한다. 왜냐하면 데코레이터는 기존함수가 어떤 입력 인수를 취할지 알 수 없기 때문이다. 따라서 이렇게 전달받아야 하는 기존 함수의 입력 인수를 알 수 없는 경우에는 `*args`와 `**kwargs` 기법을 이용하여 해결해야 한다.

| **`*args`, `**kwargs`**<br/><br/>`*args`는 모든 입력 인수를 튜플로 변환해 주는 매개변수이고 `**kwargs`는 모든 key=value 형태의 입력 인수를 딕셔너리로 변환해 주는 매개변수이다. |
| ------------------------------------------------------------ |

아래와 같은 인자를 갖는 함수를 호출한다고 한다면,

```
def func(*args, **kwargs):
    print(args)
    print(kwargs)   
    
# 수행
func(1, 2, 3, name="foo", age=3)
```

위와 같이 func 함수에 `*args`, `**kwargs` 매개변수를 사용하면 다양한 입력 인수를 모두 처리할 수 있다. 

1, 2, 3 과 같은 일반적인 입력은 args 튜플에 저장되고 name='foo' 와 같은 형태의 입력은 kwargs 딕셔너리에 저장된다.

[실행결과]

```
(1, 2, 3)
{'name': 'foo', 'age': 3}
```

그래서 다음과 같이 해당 함수부분을 수정했다.

```
import time

def elapsed(origianl_func): 
    """
    Parameters
    ----------
    origianl_func : function
        수행시간 측정
    Returns
    -------
    wrapper.

    """
    def wrapper(*args, **kwargs):
        """
        args - 튜플형태로 인자를 받음
        kwargs - 키,값 형태의 딕셔너리 타입
        """
        start  = time.time()
        result = origianl_func(*args, **kwargs) # 기존 함수 수행
        end = time.time()
        print("함수 수행시간 : %f 초" %(end - start)) # 기존 함수의 수행시간 측정
        return result  # 기존 함수의 수행결과를 리턴
    return wrapper        

@elapsed
def myfunc(msg):
    print("'%s'를 출력합니다." %msg)  


myfunc("You need python")
```

wrapper 함수의 매개변수로 `*args`와 `**kwargs`를 추가하고 기존 함수 수행시 `*args`와 `**kwargs`를 인수로 전달하여 호출

결과는 다음과 같다.

```
'You need python'를 출력합니다.
함수 수행시간 : 0.001002 초
```

## 03 이터레이터와 제너레이터

간단하게 사용하는 리스트의 반복 예를 하나 들어보자

```
for a in [1, 2, 3]:
    print(a)
```

위와 같이 반복이 가능한 객체를 iterable객체라고 한다.

### 이터레이터란?

그렇다면 이터레이터(iterator)란 무엇일까?

이터레이터는 next 함수 호출 시 계속 그 다음 값을 리턴해 주는 객체이다. 리스트는 iterable하다는 것을 이미 알아보았다. 그렇다면 리스트는 iterator일까? 다음과 같이 확인 해 보자.

```
a =[1, 2, 3]
next(a)   
```

호출했더니 에러가 난다. 리스트는 Iterable객체가 아닌가?

그렇다. 반복가능하다고 해서 - iterable - iterable객체는 아닌것이다.

```
raceback (most recent call last):

  File "C:\Users\cello\.spyder-py3\temp.py", line 6, in <module>
    next(a)

TypeError: 'list' object is not an iterator
```

하지만 iterable하다면 다음과 같이 iter 함수를 이용하여 이터레이터로 만들 수 있다.

```
>>> a = [1, 2, 3]
>>> ia = iter(a)
>>> type(ia)
<class 'list_iterator'>
```

`next함수`를 호출하면 next를 호출할때 마다 순서대로 값이 출력됨을 알 수 있다.

이터레이터는 더 이상 반환할 값이 없을 때는 StopIterator 예외가 발생하게 된다.

하지만 이터레이터의 값을 가져오는 가장 일반적인 방법은 다음과 같이 for문을 이용하는 것이다.

```
>>> next(ia)
1
>>> next(ia)
2
>>> next(ia)
3
>>> next(ia)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

```
>>> a = [1, 2, 3]
>>> ia = iter(a)
>>> for i in ia:
...     print(i)
```

이터레이터는 for문을 이용하여 반복하고 난 후에는 다시 반복하더라도 더 이상 그 값을 다시 가져오지 못한다. 이터레이터는 next로 그 값을 읽어 들이면 다시 그 값을 읽을 수 없는 특징이 있다.

### 이터레이터 만들기

리스트를 iter 함수를 이용하여 이터레이터로 만들 수 있었다. 이번에는 iter함수를 이용하지 말고 직접 이터레이터를 만드는 방법에 대해서 알아보자.

이터레이터는 클래스에 <span style="color:red">`__iter__` 와 `__next__`</span>라는 두개의 메서드를 구현하면 만들 수 있다.

다음의 예를 보자.

```
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result
    

if __name__ == "__main__":
    i = MyIterator([1, 2, 3])
    
    for item in a:
        print("항목 출력", item, end=' ')
```

MyIterator 클래스는 이터레이터 객체를 생성하기 위하여 `__iter__` 메서드와 `__next__` 메서드를 구현하였다. 

`__iter__` 메서드는 이터레이터 객체를 리턴해 주는 메서드이므로 MyIterator 클래스에 의해 생성되는 객체를 의미하는 self를 리턴하도록 했다.

 `__next__` 메서드는 next 함수 호출 시 수행되므로 MyIterator 객체 생성시 전달한 데이터를 하나씩 리턴하도록 하고 더 이상 리턴할 값이 없게 되면 StopIteration 예외를 발생시키도록 구현.

이제 위 코드를 실행하면 다음과 같은 결과를 확인 할 수 있다.

```
runcell(0, 'C:/Users/cello/.spyder-py3/temp.py')
항목 출력 1 항목 출력 2 항목 출력 3 
```

이번에는 역순으로 출력되도록 해보자

```
class ReverseItertor:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data) - 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result
    

if __name__ == "__main__":
    i = ReverseItertor([1, 2, 3, 4, 5])
    
    for item in i:
        print("역순출력", item, end=' ')
```

실행결과는 다음과 같다.

```
역순출력 5 역순출력 4 역순출력 3 역순출력 2 역순출력 1 
```

### 제너레이터란?

보통 함수는 하나의 값을 리턴한다. 그 값은 정수, 리스트, 딕셔너리등이 될 수 있을 것이다. 

그런데 만약 함수가 하나의 값을 리턴하는 것이 아니라 연속된 값을 순차적으로 리턴할 수 있다면 어떨까?

이러한 개념에서 만들어진 것이 바로 제너레이터(generator)이다.

제너레이터는 이터레이터와 마찬가지로 next 호출시 그 값을 순차적으로 얻어 낼 수 있다. 

제너레이터는 순차적인 결과값을 리턴하기 위해 return 대신 yield 키워드를 사용한다.

가장 간단한 제너레이터의 예를 보자.

```
def myGen():
    yield 'a'
    yield 'b'
    yield 'c'
# 수행    
g = myGen()
print(type(g))
```

[결과]

```
<class 'generator'>
```

순차적으로 실행시마다 값을 생성해 줌을 알 수 있다.

```
print(next(g))
print(next(g))
print(next(g))
```

```
<class 'generator'>
a
b
c
```

위와 같이 제너레이터 객체 g에 next함수를 실행하면 mygen 함수의 첫번째 yield 문에 의해서 'a' 값이 리턴된다. 

여기서 재밌는 점은 제너레이터는 **yield**라는 문장을 만나게 되면 그 값을 리턴하고 현재의 상태를 그대로 기억한다는 점이다. 

이건 마치 음악 플레이어를 재생하다가 포즈(pause)로 멈추어 놓은 것과 비슷한 모양새이다. 이러한 방식을 전문 용어로 **코루틴(Coroutine)**이라고 한다.

> 제너레이터는 이러한 이유로 코루틴(coroutine)이라고도 불리운다.

> 모든 제너레이터는 이터레이터를 만들어 내기 때문에 제너레이터 객체는 이터레이터라고 할 수 있다.

### 제너레이터 표현식

이번에는 다음의 예를 보자.

```
def myGen():
    for i in range(1, 1000):
        result =  i **2
        yield result        
        
gen = myGen()

print(next(gen))
print(next(gen))
print(next(gen))
```

[결과]

```
1
4
9
```

위의 제너레이터 표현식(generator expression)을 아래와 같이 튜플 comprehension으로 가능함을 기억하자.

```
gen2 = (i ** 2 for i in range(1, 1000))
```

### 제너레이터와 이터레이터

지금까지 살펴본 제너레이터는 이터레이터와 상당히 비슷하다는 것을 알 수 있다. 

클래스를 이용하여 이터레이터를 작성하면 좀 더 복잡한 행동을 하도록 만들 수 있다. 

반면에 제너레이터 표현식 같은 것을 이용하면 정말 간단하게 이터레이터를 만들 수 있다. 

따라서 여러분이 만들어 낼 이터레이터의 성격에 따라 클래스로 작성할 것인지 제너레이터로 작성할 것인지를 선택해야 한다.

보통 간단한 경우라면 제너레이터 함수나 제너레이터 표현식을 사용하는 것이 가독성 및 유지보수 측면에서 유리하다.

다음은 `(i * i for i in range(1, 1000))` 제너레이터를 이터레이터 클래스로 구현한 예이다.

```
class MyIterator:
    
    def __init__(self):
        self.data = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.data ** 2
        self.data += 1
        if self.data >= 1000:
            raise StopIteration
        result result
```


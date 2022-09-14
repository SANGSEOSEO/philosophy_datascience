# Numpy ndarray

ndarray : N차원(Dimension)배열 (Array) 객체

![ndarray drawio](https://user-images.githubusercontent.com/70785000/190153543-5906ec3d-e41a-4bfb-b8c0-a267bce7ce87.png)


* 1차원 배열은 선의 개열
* 2차원 배열은 1차원의 요소가 여러개 있는 것을 의미
* 3차원 배열 - 면적이 - 2차원 배열- 여러 개 있다고 이해하자.

 

## ndarray 생성

```python
import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([[1, 2, 3], [2, 3, 4]])
```

```python
## 실행결과는 다음과 같다.
[1 2 3]  # array1
[[1 2 3] [2 3 4]] # array2
```

Numpy모듈의 array() 함수로 생성하며 , 인자로 주로 파이썬의 list혹은 ndarray를 입력받는다.



## ndarray형태 (Shape) 와 차원

| array              | 차원(Dimension) | Shape                    |
| ------------------ | ------------- | ------------------------ |
| `[1,2,3]`          | 1차원           | (3,)  <-- 1차원            |
| `[[1,2,3][4,5,6]]` | 2차원           | (2,3) - 행의 갯수 2, 열의 갯수 3 |

ndarray의 shape은 ndarray.shape속성의로 , 차원은 ndarray.ndim속성으로 알수 있습니다. 

## ndarray타입(type)

```python
[1,2,3]
[1.1 2.1 3.2]
['홍길동' '임꺽정']
[True False True]
```

* ndarray내의 데이터 값은 숫자 값, 문자열 값, 불린 값 등이 모두 가능
* 숫자형의 경우 int형(8bit, 16bit, 32bit), unsigned int형(8bit, 16bit, 32bit) , float형(16bit, 32bit, 64bit, 128bit), 그리고 이보다 더 큰 숫자 값이나 정밀도를 위해 complex타입로 제공
* ndarray내의 데이터 타입은 그 연산의 특성상 같은 데이터 타입만 가능합니다. 즉, 한 개의 ndarray객체에 int와 float가 공존 할 수 없다. 그런 경우엔 int, float과 공존하는 데이터의 int형을 float형으로 변환한다.
* ndarray내의 데이터 타입은 ndarray.dtype으로 확인 가능

## ndarray타입 변환

### astpye()를 이용하여 변환

* 변경을 원하는 타입을 astype() 에 인자로 입력
* 대용량 데이터를 ndarray로 만들때 메모리를 절약하기 위해 자주 사용
* 0,1,2와 같이 크지 않는 범위의 숫자를 위해서 64bit float형 보다는 8비트  혹은 16비트의 integer형으로 변환하는 것이 훨씬 메모리를 많이 절약하게 됨

> 대용량 데이터를 다룰 시 메모리 절약을 위해서 형변환을 특히 고려해야 함.
>
> 사용 예)

```python
import numpy as np
array1d = [1.0, 2.0]
array1d.astype("int32")  # array1d.astype(np.int32)
```


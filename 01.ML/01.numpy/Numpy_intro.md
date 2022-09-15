# Numpy ndarray

ndarray : N차원(Dimension)배열 (Array) 객체

![ndarray drawio](https://user-images.githubusercontent.com/70785000/190153543-5906ec3d-e41a-4bfb-b8c0-a267bce7ce87.png)


* 1차원 배열은 각 원소들이 선분처럼 배열된 것으로 이해
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

## ndarray sum function using axis

<img width="369" alt="numpy_axis" src="https://user-images.githubusercontent.com/70785000/190310650-e1c6f57f-c076-4439-bfa4-73d483a84a8d.png">

* calculation with axis

  ```python
  np_array_2d = np.arange(0, 6).reshape(2,3)
  print(np_array_2d)
  ```

  ```python
  [[0 1 2]
   [3 4 5]]
  ```

  ```python
  np.sum(np_array_2d,axis=0)
  ```

  ```python
  # execution result
  array([3, 5, 7])
  ```

  ```python
  np.sum(np_array_2d, axis=1)
  ```

  ```python
  # execution result
  array([ 3, 12])
  ```

  |                 axis =0                  |                 axis = 1                 |
  | :--------------------------------------: | :--------------------------------------: |
  | <img width="176" alt="axis_0" src="https://user-images.githubusercontent.com/70785000/190311628-dc69d296-9e9a-4d28-902e-5868055e7265.png"> | <img width="203" alt="axis_1" src="https://user-images.githubusercontent.com/70785000/190311979-cc6e7162-fe99-4a7a-9b5e-cb58184ba102.png"> |


## ndarray를 편리하게 생성 및 변경

> arange, zeros, ones, reshape

* 특정 크기와 차원을 가진 ndarray를 연속값이나 0또는 1로 초기화 생성해야 할 경우 arange(), zeros(), ones()를 이용해 쉽게 ndarray를 생성 할 수 있습니다. 주로 테스트용으로 데이터를 만들거나 데이터를 일괄적으로 초기화해 사용 할 경우에 적용 가능

```python
np.arange(10)
```

```python
# 실행결과
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

```python
np.zeros((3,2), dtype='int32') # int32타입의 영행렬을 생성, 행이 3개이고, 컬럼 갯수는 2개
```

```python
# 실행결과
array([[0, 0],
       [0, 0],
       [0, 0]])
```

```python
np.ones((3,2))  # dtype를 주지 않으면 float64형으로 생성
```

```python
# 실행결과
array([[1., 1.],
       [1., 1.],
       [1., 1.]])
```

* reshape()는 ndarray를 특정 차원 및 형태로 변환. 변환 형태를 함수 인자로 부여할 수 있다.

  ```python
  x = np.arange(10)
  print(x.reshape((2, 5), order='C'))
  ```

* reshape()는 reshape(-1, 1), reshape(-1,) 과 같은 형식으로 변환이 되는 요구 경우, 주로 머신러닝 API의 인자로 1차원 ndarray를 명확하게 2차원 ndarray로 변환하여 입력하기를 원하거나, 또는 반대의 경우가 있을 경우 reshape()를 이용하여 ndarray의 형태를 변환시켜주는 데 사용

  ```python
  array1d = np.array([0, 1, 2, 3, 4])
  array2d = array1d.reshape((-1, 1))  # 2차원이고 , 컬럼의 갯수 1개
  print(f"array2d shape : {array2d.shape}, array2d : \n {array2d}, \n{array2d.ndim} 차원")
  ```

  ```python
  # result
  array2d shape : (5, 1), 
  array2d : 
   [
   [0]
   [1]
   [2]
   [3]
   [4]
   ], 
  2 차원
  ```

  ```python
  print(f'Array2d : \n {array2d}')
  array_conv = array2d.reshape(-1,)    # 1차원으로 변환
  print(f"변환된 행렬 : {array_conv}, 변환된 행렬의 shape : {array_conv.shape}, 변환된 행렬의 차원 : {array_conv.ndim}")
  ```

  ```python
  # result
  Array2d : 
   [[0]
   [1]
   [2]
   [3]
   [4]]
  변환된 행렬 : [0 1 2 3 4], 변환된 행렬의 shape : (5,), 변환된 행렬의 차원 : 1
  ```

## ndarray의 데이터 세트 선택 - 인덱싱(Indexing)

|          인덱싱 유형          | 설명                                       |
| :----------------------: | :--------------------------------------- |
|      특정 위치의 단일값 추출       | 원하는 위치의 인덱스 값을 지정하면 해당 위치의 데이터가 반환<br />ex) 파이썬의 인덱싱과 유사함 |
|      슬라이싱(Slicing)       | 슬라이싱은 연속된 인덱스상의 ndarray를 추출하는 방식.`:` 기호 사이에 시작 인덱스와 종료 인덱스를 표시하면 시작 인덱스에서 종료 인덱스 `-1`위치에 있는 ndarray를 반환합니다. <br />예를 들어 1:5라고 하면 시작 인덱스 1과 종료 인덱스 4까지에 해당하는 ndarray를 반환<br />ex)파이썬의 슬라이싱 방식과 유사함 |
|  팬시 인덱싱(Fancy Indexing)  | 일정한 인덱싱 집합을 리스트 또는 ndarray형태로 지정해 해당 위치에 있는 ndarray를 반환 |
| 불린 인덱싱(Boolean Indexing) | 특정 조건에 해당하는지 여부인 True/False값 인덱싱 집합을 기반으로 True에 해당하는 인덱스 위치에 있는 ndarray를 반환 |

### 팬시 인덱싱 - 1차원 ndarray

* 팬시 인덱싱(Fancy Indexing)은 리스트 혹은 ndarray로 인덱스 집합을 지정하면 해당 위치의 인덱스에 해당하는 ndarray를 반환하는 인덱싱 방식입니다.

![fancy_indexing](https://user-images.githubusercontent.com/70785000/190357894-91a5ea72-55d3-4eb7-81b2-764364af7cce.png)

* 인덱싱하고자 하는 대상은 Python List의 형태 혹은 numpy.ndarray 타입니다.

### 팬시 인덱싱 - 2차원 ndarray

![fancy_indexing_2 drawio](https://user-images.githubusercontent.com/70785000/190409337-3341fe0c-596c-4de8-9a8a-22892c0f976a.png)

* array2d[[0,1]]의 의미는 axis = 0만 있다는 의미(행만 해당, 컬럼은 전부 포함된다는 의미)



### 불린 인덱싱 - 1차원 ndarray

* 불린 인덱싱(boolean indexing) 은 조건 필터링과 추출을 동시에 할 수 있기 때문에 매주 자주 사용되는 인덱싱 방식.

* boolean condition을 `[]`에 입력 -> `False`값은 무시하고 `True`값에 해당하는 Index값만 저장

  -> 저장된 인덱스 값으로 데이터를 조회

* 만약 , ndarray내의 값이 5보다 큰 ndarray를 추출하고자 한다면?

  ```python
  # 불린 인덱싱을 사용하지 않는 경우
  array1d = np.arange(start = 1, stop=10)
  target = []

  for i in range(0, 9):
    if array1d[i] > 5:
      target.append(array1d[i])
      
  array_selected = np.arrany(target)
  ```

  ```python
  # 불린 인덱싱을 사용하는 경우
  array1d = np.arange(start=0, stop=10)
  array1d[array1d > 5]  # 이렇게 하면 된다.
  ```

  ```python
  # array1d result
  [0 1 2 3 4 5 6 7 8 9]
  # boolean index result
  boolean index result : [6 7 8 9]
  ```

### 배열의 정렬 - sort() 와 argsort()

#### sort()

*  `np.sort(ndarray)` - 인자로 들어온 원 행렬은 그대로 유지한 채 원 행렬의 정렬된 행렬을 반환
* `ndarray.sort()`는 원 행렬 자체를 정렬한 형태로 변환하며 반환 값은 `None`

> `np.sort()` 나 `ndarray.sort()` 모두 기본적으로 오름 차순으로 행렬 내 원소를 정렬합니다. 
>
> 내림 차순으로 정렬하기 위해서는 `[::-1]`를 적용합니다. 
>
> `np.sort()[::-1]`과 같이 사용하면 됩니다.

* 2차원 배열에서의 `axis`기반의 	`sort()` 기본적으로 올림차순임을 기억하자

  np.sort(A, axis = 0)를 소팅한다고 가정한다면 이렇게?
  $$
  \begin{bmatrix}                                          
  8 & 12 \\
  7 & 1
  \end{bmatrix}
  \Rightarrow
  \begin{bmatrix}                                          
  7 & 1 \\
  8 & 12
  \end{bmatrix}
  $$


​     np.sort(A, axis = 1) 를 소팅한다고 가정
$$
\begin{bmatrix}                                          
8 & 12 \\
7 & 1
\end{bmatrix}
\Rightarrow
\begin{bmatrix}                                          
8 & 12 \\
1 & 7
\end{bmatrix}
$$

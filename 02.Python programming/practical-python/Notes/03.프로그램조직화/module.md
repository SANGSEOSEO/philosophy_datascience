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

#### <span style="color:red">import as</span> 문




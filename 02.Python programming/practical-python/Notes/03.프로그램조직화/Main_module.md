# 메인 모듈

이번 장에서는 메인 프로그램과 메인 모듈에 대한 개념을 소개할 것이다.

## 메인 함수

```c
// c / c++
int main(int argc, char *argv[]) {
    ...
}
```

```java
// java
class myprog {
    public static void main(String args[]) {
        ...
    }
}
```

## 파이썬 메인 모듈

파이썬은 `main`이라는 함수 혹은 메소드가 없으나, `메인 모듈` 이라는 가장 먼저 수행되는 프로그램이 있다.

### `__main__` check

```python
# prog.py
...
if __name__ == '__main__':
    # Running as the main program ...
    statements
    ...
```

### Main programs vs. library imports

<span style="color:red">__name__</span> 은 모듈의 이름이고, <span style="color:red">__main__</span>으로 정의됨.

임포트시에 자동으로 실행이 되는 문제가 있는데 이런 경우엔 아래와 같이 추가해야 한다.

```python
if __name__ == '__main__':
    # Does not execute if loaded with import..
```

### 프로그램 템플릿

```python
# prog.py
# Import statements (libraries)
import modules

# Functions
def spam():
    ...

def blah():
    ...

# Main function
def main():
    ...

if __name__ == '__main__':
    main()
```

### CLI (커맨트라인 툴)

셀상 혹은 커맨트라인 모드에서 스크립트가 수행 가능

```python
bash % python3 report.py portfolio.csv prices.csv
```

이러한 텍스트 열의 리스트를 <span style="color:red">_`sys.argv`</span>에서 찾을 수 있다.

```python
# 위 bash 명령에서
sys.argv # ['report.py, 'portfolio.csv', 'prices.csv']
```

인자를 처리하는 예

```python
import sys

if len(sys.argv) != 3:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
portfile = sys.argv[1]
pricefile = sys.argv[2]
...
```

### 표준입출력(Standard I/O)

표준입출력 파일(Standard Input / Oupput file- stdio)은 일반 파일과 동일하게 동작함.

```python
>>> import sys
>>> sys.stdout
<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
>>> sys.stderror
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'sys' has no attribute 'stderror'
>>> sys.stderr
<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
>>> sys.stdin
<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>
```

print명령어는 바로 sys.stdout으로 전달되고 Input은 sys.stdin을 통해 읽혀진다.

traceback과 error는 sys.stderr을 통해 에러의 추적이 가능하다.

*stdio*는 터미널, 파일, 파이프 등에 연결될 수 있다.

### 환경변수

환경변수(Environment variable)는 터미널 혹은 쉘에서 셋업이 가능하며,     다음과 같이 확인이 가능

아래와 같이 dictionary 타입임을 알수있다.

```python
>>> import os
>>> os.environ
environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\서한나\\AppData\\Roaming', 'ASL.LOG': 'Destination=file', 'CLASSPATH': '%classpath%;;;', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6
432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'SANGSEOSEO', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'CONFIGSETROOT': 'C:\\WINDOWS\\ConfigSetRoot', 'FP_NO_HOST_CHECK': 'NO', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\서한나', 'JAVA_HOME': 'C:\\jdk-11.0.6', 'LOCALAPPDATA': 'C:\\Users\\서
한나\\AppData\\Local', 'LOGONSERVER': '\\\\SANGSEOSEO', 'NUMBER_OF_PROCESSORS': '4', 'OS': 'Windows_NT', 'PATH': ';C:\\oraclexe\\app\\oracle\\product\\11.2.0\\server\\bin;;C:\\jdk-11.0.6\\bin;C:\\Program Files (x86)\\Wizvera\\Delfino;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\I
ntel\\iCLS Client\\;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\Windows Live\\Shared;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine C
omponents\\IPT;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files (x86)\\Intel\\OpenCL SDK\\3.0\\bin\\x86;C:\\Program Files (x86)\\Intel\\OpenCL SDK\\3.0\\bin\\x64;C:\\Program Files\\
Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\;C:\\Users\\서한나\\AppData\\Local\\Programs\\Python\\Python38;C:;Users\\서한나\\AppData\\Local\\Programs\\Python\\Python38\\Scripts;%M;SQL_HOME%\\bin;C:\\Users\\서한나\\Desktop\\SQLiteDatabaseBrowserPortable;;;;:\\Program Fi
les\\Git\\cmd;C:\\Program Files\\Git\\cmd;C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files\\Graphviz 2.44.1\\bin\\dot.exe;C:\\anaconda3\\Lib\\site-packages\\graphviz;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Inte
l\\WirelessCommon\\;C:\\Users\\서한나\\AppData\\Local\\atom\\bin;C:\\jdk-11.0.6\\bin;C:\\jdk-11.0.6\\bin;C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files\\Graphviz 2.44.1\\bin;C:\\Microsoft VS Code\\bin;C:\\Program Files (x86)\\ESTsoft\\ALSe
e\\x64', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 69 Stepping 1, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '4501', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\P
rogram Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '$P$G', 'PSMODULEPATH': 'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS'
, 'TEMP': 'C:\\Users\\서한나\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\서한나\\AppData\\Local\\Temp', 'UOIPME_REG_PATH': 'C:\\Program Files\\Intel Corporation\\USB over IP', 'USERDOMAIN': 'SANGSEOSEO', 'USERDOMAIN_ROAMINGPROFILE': 'SANGSEOSEO', 'USERNAME': '서한나', 'USERPROFILE': 'C:\\Users\\서한
나', 'WINDIR': 'C:\\WINDOWS'})
```

아래와 같이 특정키만 가져올 수 있다.

```python
>>> os.environ['PATH']
';C:\\oraclexe\\app\\oracle\\product\\11.2.0\\server\\bin;;C:\\jdk-11.0.6\\bin;C:\\Program Files (x86)\\Wizvera\\Delfino;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Progra
owerShell\\v1.0\\;C:\\Program Files (x86)\\Windows Live\\Shared;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Managemen
\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files (x86)\\Intel\\OpenCL SDK\\3.0\\bin\\x86;C:\\Program Files (x86)\\Intel\\OpenCL SDK\\3.0\\bin\\x64;C:\\Progr
ograms\\Python\\Python38;C:;Users\\서한나\\AppData\\Local\\Programs\\Python\\Python38\\Scripts;%M;SQL_HOME%\\bin;C:\\Users\\서한나\\Desktop\\SQLiteDatabaseBrowserPortable;;;;:\\
e Data Studio\\bin;C:\\Program Files\\Graphviz 2.44.1\\bin\\dot.exe;C:\\anaconda3\\Lib\\site-packages\\graphviz;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common F
ram Files\\MySQL\\MySQL Server 8.0\\bin;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files\\Graphviz 2.44.1\\bin;C:\\Microsoft VS Code\\bin;C:\\Program Files (x86)\\EST
```

### 프로그램 종료(Program exit)

Exception을 통해 프로그램 종료 가능

```python
raise SystemExit
raise SystemExit(exitcode)
raise SystemExit('Informative message')
```

다른 대안

```python
import sys
sys.exit(exitcode)
```

### `#!` 행

유닉스에서 <span style="color:red">`#!`</span> 행은 스크립트를 파이썬으로서 실행할 수 있다. 다음과 같이 스크립트 파일 첫행에 추가한다.

```python
#!/usr/bin/env python3
# prog.py
...
```

당연히 실행권한이 필요

```python
bash % chmod +x prog.py
# Then you can execute
bash % prog.py
... 출력 ...
```

### 스크립트 템플릿

```python
#!/usr/bin/env python3
# prog.py

# Import statements (libraries)
import modules

# Functions
def spam():
    ...

def blah():
    ...

# 메인 함수
def main(argv):
    # 명령행 인자, 환경 변수 등을 파싱.
    ...

if __name__ == '__main__':
    import sys
    main(sys.argv)
```



### 연습문제 3.15 main()함수 

```python
bash % python3 report.py portfolio.csv prices.csv
```

```python
C:\dataAnalysis\philosophy_datascience\02.Python programming\practical-python\Notes\03.프로그램조직화>python report.py portfolio.csv prices.csv
첫번째 파라미터 :  report.py
두번째 파라미터 :  portfolio.csv
세번째 파라미터 :  prices.csv
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

### 연습문제 3.16 main() 함수 

```python
C:\dataAnalysis\philosophy_datascience\02.Python programming\practical-python\Notes\03.프로그램조직화>python pcost.py portfolio.csv
Total cost :  44671.15
```




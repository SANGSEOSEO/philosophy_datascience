import re

p = re.compile("a.b")

# \n은 .메타문자와는 매치되지 않음
m = p.match("a\nb")
print("DOTALL : ", m)

p1 = re.compile("a.b", re.DOTALL)

#DOTALL컴파일 옵션은 \n문자와 매치됨됨
m1 = p1.match("a\nb")
print(m1)

p = re.compile("[a-z]", re.IGNORECASE)
m = p.match("python")
print(m)

m = p.match("Python")
print(m)

m = p.match("PYTHON")
print(m)


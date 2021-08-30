import re

p = re.compile('[a-z]+')
m = p.match("python")
print(m.group())  # 매치되는 문자열 리턴
print(m.start())  # match메소드는 항상 문자열의 시직부터 조사하므로.
print(m.end())
print(m.span())
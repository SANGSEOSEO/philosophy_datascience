import re
p = re.compile("^python\s\w+") # python으로 시작하고 공백다음에 단어가 1개 이상 있는 문자열만 매치

data = """python one
Life is too short
python two
you need python
python three"""

print(p.findall(data))

p = re.compile("^python\s\w+", re.MULTILINE)
multiline = p.findall(data)
print("re.MULTILINE적용: ", multiline)
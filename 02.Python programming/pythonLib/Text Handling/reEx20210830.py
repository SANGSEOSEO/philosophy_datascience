import re


p = re.compile('[a-z]+')  # 앞의 문자가 1번 이상 나오는 것

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

m = p.search("python")
print("re.search()", m)

m = p.search("3 python")
print("숫자가 같이 있는 경우: ", m)


# findall
result = p.findall("life is too short")
print("findall : ", result)

# finditer

result = p.finditer("life is too short")
print("finditer() result : ", result)

for r in result:
    print(r)
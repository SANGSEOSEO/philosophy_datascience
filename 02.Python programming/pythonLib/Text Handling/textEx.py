import textwrap

long_text = "Life is too short. You need python" * 10

# shorten into 70bytes
print(textwrap.shorten(long_text, width=70, placeholder="..."))

# wrap into 70bytes
result = textwrap.wrap(long_text,width=70)
print("70바이트만큼씩 줄바꿈", result)

#고정폭 문자열로 표시
print("\n".join(result))

#fill함수 사용하여 70바이트씩 줄바꿈하고 이것을 문자열로 표시
print(textwrap.fill(long_text, width=70))
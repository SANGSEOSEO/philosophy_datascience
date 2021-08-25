import textwrap as tw

text =  "Life is too short, you need python."
print(tw.shorten(text, width=15))

kor_text = "인생은 짧으니 파이썬이 필요해"
print(tw.shorten(kor_text, width=15))
print(tw.shorten(kor_text,placeholder='...', width=15))



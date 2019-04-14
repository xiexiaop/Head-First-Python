# 输入字符：Don't panic
# 作处理后输出字符：on tap

phrase = "Don't panic"
plist = list(phrase)
print(phrase)
print(plist)

plist.remove("D")
for i in range(3):
    plist.pop()
plist.remove("'")
plist.insert(2," ")
plist.pop(4)
plist.insert(4,"a")
plist.pop()

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)


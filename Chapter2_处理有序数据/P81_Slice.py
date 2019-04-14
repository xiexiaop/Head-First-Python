# 以切片方式实现Don't panic转换为 on tap
phrase = "Don't panic"
plist = list(phrase)
print(phrase)
print(plist)
new_phrase = ''.join(phrase[1:3:1])
new_phrase = new_phrase + ''.join([plist[5],plist[4],plist[7],plist[6]])
print(plist)
print(new_phrase)

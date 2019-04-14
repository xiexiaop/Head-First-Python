# 通过操作列表认识开始，结束，步长
# 理解切片
# word = "Don't panic"
# letters = list(word)
# print(letters[0:10:3])
# print(letters[3:])
# print(letters[:10])
# print(letters[::2])

book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print(booklist)
print(booklist[0:3])
print(''.join(booklist[0:3]))
print(''.join(booklist[-6:]))
# 翻转字符串
print(''.join(booklist[::-1]))
# 每2个字符拼接到一起
print(''.join(booklist[::2]))

# 取出单词Hitchhiker
print(''.join(booklist[4:14:]))
# 取出单词Hitchhiker逆序显示
print(''.join(booklist[13:3:-1]))





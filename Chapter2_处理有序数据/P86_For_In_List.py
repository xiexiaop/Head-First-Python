# Python的“for”循环了解列表
# a = "Marvin"
# letters = list(a)
# for char in letters:
#     print('\t',char)


# Python的“for”循环了解切片
a = "Marvin,the Paranoid Android"
letters = list(a)
for char in letters[:6]:
    print('\t', char)

for char in letters[-7:]:
    print('\t'*2, char)

for char in letters[12:20]:
    print('\t'*3, char)

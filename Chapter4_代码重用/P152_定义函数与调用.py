# 1.函数定义与调用
# def search4Vowels():
# """DOCSTRING"""
#     vowels = set('aeiou')
#     word = input("Provide a word to search for vowels")
#     found = vowels.intersection(set(word))

#     for vowel in found:
#         print(vowel)


# search4Vowels()

# 2.带参数的函数定义与调用
# def search4Vowels(word):
#     """DOCSTRING"""
#     vowels = set('aeiou')
#     found = vowels.intersection(set(word))

#     for vowel in found:
#         print(vowel)


# search4Vowels('love')

# 3.带返回值[布尔值]的函数定义与调用
# def search4Vowels(word):
#     """DOCSTRING"""
#     vowels = set('aeiou')
#     found = vowels.intersection(set(word))
#     return bool(found)

# print(search4Vowels('love'))


# 4.带返回值[对象]的函数定义与调用
def search4Vowels(word):
    """DOCSTRING"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))

print(search4Vowels('love'))
print(search4Vowels('sky'))




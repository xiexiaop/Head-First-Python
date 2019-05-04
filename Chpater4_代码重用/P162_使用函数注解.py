# 1.使用函数注释
# def search4Vowels(word:str) ->set():
#     """DOCSTRING"""
#     vowels = set('aeiou')
#     return vowels.intersection(set(word))

# print(search4Vowels('love'))


# 2.更通用的2个字符串交集
# def search4Letters(phrase:str,letters:str) ->set():
#     """Return a set of the 'letters' found in phrase"""
#     return set(letters).intersection(set(phrase))


# print(search4Letters('life','ife'))


# 3.设置函数参数默认值
# def search4Letters(phrase:str, letters:str='aeiou') ->set:
#     """Return a set of the 'letters' found in phrase"""
#     return set(letters).intersection(set(phrase))


# print(search4Letters('life'))


# 4.位置赋值
# def search4Letters(phrase:str, letters:str='aeiou') ->set:
#     """Return a set of the 'letters' found in phrase"""
#     return set(letters).intersection(set(phrase))


# print(search4Letters('life','ao'))


# 5.关键字赋值
def search4Letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in phrase"""
    return set(letters).intersection(set(phrase))

print(search4Letters(letters='ao',phrase='life'))

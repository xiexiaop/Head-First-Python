# 使用集合实现单词中查找元音
vowels = {'a', 'e', 'i', 'o', 'u'}
word = input("Provide a word to search for vowels")
found = vowels.intersection(set(word))

for vowel in found:
    print(vowel)
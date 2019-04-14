# 在一个英文单词中寻找包含原音的英文字母
# 步骤一：找到即输出所有原音
# vowels = ['a','e','i','o','u']
# word = "Milliways"

# for letter in word:
#     if letter in vowels:
#         print(letter)

# # 步骤二：找到即输出所有原音［不重复］
# vowels = ['a','e','i','o','u']
# found = []
# word = "Milliways"

# for letter in word:
#     if letter in vowels and letter not in found:
#         found.append(letter)
        
# for vowel in found:
#     print(vowel)

# 步骤三：提供前台用户输入英文字符
vowels = ['a','e','i','o','u']
found = []
word = input("Provide a word to search for vowels")

for letter in word:
    if letter in vowels and letter not in found:
        found.append(letter)
        
for vowel in found:
    print(vowel)

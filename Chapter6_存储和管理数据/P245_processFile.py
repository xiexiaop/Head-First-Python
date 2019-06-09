# todos = open('todos.txt')
# for chore in todos:
#     print(chore)
# todos.close()


with open('todos.txt') as todos:
    for chore in todos:
        print(chore)

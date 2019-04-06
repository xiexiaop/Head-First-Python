# 广度优先搜索
from collections import deque


def person_is_seller(name):
    return name[-1] == "m"


def search(name):
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["annuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["annuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + " is a mango seller")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return False


search("you")

# 算法：
# 1.只要还有要处理的节点
# 2.获取离当前节点最近的节点
# 3.更新当前节点邻居的开销
# 4.如果有邻居的开销被更新,同时更新邻居的父节点
# 5.将该节点标记为已处理
# 6.找下下一个节点并执行1-5

# 定义与图相关的所有散列表-Begin
# 第一个散列表存取每个节点前往邻居节点的权重值
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# 第二个散列表存取从起点开始前往其他点的开销
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = float("inf")

# 第三个散列表存取从出起点外其他节点的父节点
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 第四个散列表存取已经处理过的节点
processed = []
# 定义与图相关的所有散列表-End

# 找到从某一节点前往其所有邻居节点中开销最小的节点


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 开始处理节点寻找权重值最小的路径
# 最短时间


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(new_cost)

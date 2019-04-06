# 假设你办了个广播节目，要让全美50个州的听众都收听得到。为此你需要决定在哪些广播台播出。
# 在每个广播台播出都需要支付费用，因此你力图在尽可能少的广播台播出。
# 使用贪婪算法可得到非常接近的解：
# 1、选出这样一个广播台，即它覆盖了最多的未覆盖州，即便这个广播台覆盖了一些一覆盖的州也没有关系；
# 2、重复第一步，直到覆盖了所有的州。


# 创建一个列表，其中包含要覆盖的州
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
# 创建广播台清单
stations = {}
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])

# 创建一个集合来存储最终选择的广播台
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)

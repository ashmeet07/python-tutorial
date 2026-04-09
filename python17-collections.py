from collections import Counter, defaultdict, deque, OrderedDict, ChainMap

#Counter for hasing
data = ["a", "b", "a", "c", "b", "a"]
count=Counter(data)#hash man do frequency count auto
print(count)

#Defaultdict
data=defaultdict(list)
data["a"].append(1)
print(data)
print(defaultdict(int),defaultdict(float),defaultdict(set))

#Dequeue
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)

print(dq)


#order dict in python 3.7+ have it 
od = OrderedDict()
od["a"] = 1
od["b"] = 2


#Chaining dictionaris in using ChainMap 
d1 = {"a": 1}
d2 = {"b": 2}

cm = ChainMap(d1, d2)
print(cm["a"], cm["b"])
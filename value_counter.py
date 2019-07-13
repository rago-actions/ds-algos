#Value counter
#method1
counter = {}
for item in items:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1

#method2
from collections import defaultdict
counter = defaultdict(int)
for item in items:
    counter[item] += 1

return counter

#method3
from collections import counter
counter = Counter(items)

#method4
for color in colors:
    d[color] = d.get(color, 0) + 1

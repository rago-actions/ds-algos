#Value counter
#method1
def length(iterator):
    count = 0
    for item in iterator:
        count += 1
    return count

def count(iterator, itm):
    count = 0
    for item in iterator:
        if item == itm:
            count += 1
    return count

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

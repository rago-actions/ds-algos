#searching for an item in unordered list
def find_item(item, itemlist):
    for i in range(0, len(items)):
        if item == itemlist[i]:
            return i
    return None

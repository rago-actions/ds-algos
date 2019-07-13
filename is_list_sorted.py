#Create a function to test whether the list is sorted or not
def is_sorted():
    for i in range(0, len(itemlist -1)):
        if (itemlist[i] > itemlist[i+1]):
            return False
    return True

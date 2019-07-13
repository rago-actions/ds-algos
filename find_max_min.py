#find max value with recusrion
def find_max(items):
   if len(items) == 1:
        return items[0]

   op1 = items[0]
   op2 = find_max(items[1:])

   if op1 > op2:
        return op1
   else:
        return op2
        

#find min value with recusrion
def find_min(items):
   if len(items) == 1:
        return items[0]

   op1 = items[0]
   op2 = find_min(items[1:])

   if op1 < op2:
        return op1
   else:
        return op2

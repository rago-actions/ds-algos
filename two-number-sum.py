#solution1
def twoNumberSum(array, targetSum):
   D = dict()
   for currentNum in array:
       MatchingNum = targetSum - currentNum
       if MatchingNum in D.keys():
          return [MatchingNum, currentNum]
       else:
          D[currentNum] = True
          
#solution2
def twoNumberSum(array, targetSum):
   for i in range(len(array) - 1):
      firstNum = array[i]
      for j in range(i+1, len(array)):
          secondNum = array[j]
          if firstNum + secondNum == targetSum:
              return [firstNum, secondNum]
   return []
 
#solution3
def twoNumberSum(array, targetSum):
   array.sort()
   left = 0
   right = len(array) - 1
   while left < right:
       currentSum == array[left] + array[right]
       if currentSum == targetSum:
           return [array[left], array[right]]
       elif currentSum < targetSum:
           left += 1
       elif currentSum > targetSum:
           right -= 1
   return []
          

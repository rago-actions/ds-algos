class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        S = []
        for i in nums:
            if i not in S:
                S.append(i)
            else:
                S.remove(i)
        return S[0]
    
#solved in leetcode.com
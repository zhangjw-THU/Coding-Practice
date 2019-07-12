class Solution(object):
    def solve(self,nums,n):
        if len(nums)<n:
            return []
        res = []
        for i in range(len(nums)-n+1):
            res.append(max(nums[i:i+n]))

        return res
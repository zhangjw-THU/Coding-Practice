

class Solution(object):
    def solve(self,s):
        """
        :param s: str
        :return:str
        """
        nums  = s.split('.')
        if len(nums)>2:
            print("input error!")
            return None
        elif len(nums) == 0:
            print("input error!")
            return None
        elif len(nums) == 1:
            return nums[0] + '.00'
        elif len(nums[1])>=2:
            return nums[0] + '.' + nums[1][0:2]
        else:
            return nums[0] + '.' + nums[1] +'0'

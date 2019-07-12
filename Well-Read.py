
import numpy as np
class Solution(object):
    def solve(self,nums_list):
        """

        :param nums_list:
        :return:
        """
        max_id = 0
        for i in range(len(nums_list)):
            if len(nums_list[i]) == 0:
                continue
            for j in range(len(nums_list[i])):
                if nums_list[i][j] >max_id:
                    max_id = nums_list[i][j]
        num_sts = np.zeros(max_id+1)
        for i in range(len(nums_list)):
            if len(nums_list[i]) == 0:
                continue
            for j in range(len(nums_list[i])):
                tmp = nums_list[i][j]
                num_sts[tmp] = num_sts[tmp] + 1

        idx = np.where(num_sts == np.max(num_sts))
        res = list(idx)[0]
        if len(res)==1 and res == [0]:
            return []
        return res


a = [[],[2,1,3,5],[],[2,1,5,6],[5]]
b = [[1,2],[2,3]]
c = [[1,2,3],[2,3,4]]
d = []
print(Solution().solve(a))

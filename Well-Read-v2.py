import collections

class Solution(object):
    def solve(self,nums_list):
        list_combine = []
        for i in nums_list:
            list_combine = list_combine + i

        b = collections.Counter(list_combine)
        c = sorted(b.items(),key=lambda x:x[1], reverse=True)
        well_reader = []
        if len(c)==0:
            return well_reader
        max_count = c[0][1]
        for i in c:
            if i[1] != max_count:
                break
            well_reader.append(i[0])

        return sorted(well_reader)



# # a = [[1,2],[2,3]]
# b = [[1,2,3],[2,3,4]]
# c = [[],[2,1,4],[2,5,2]]
# print(Solution().solve(c))
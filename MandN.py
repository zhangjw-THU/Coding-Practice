def Judge(r):
    flag = True
    for i in set(r):
        if r.count(i) > 2:
            flag = False
            break
    return flag


def find_combine(item, m, n, result):
    if n <= 0 or m <= 0:
        return
    if n == m:
        tmp = item + [m]
        if Judge(tmp):
            result.append(tmp)
    item.append(m)# m 在集合当中
    find_combine(item, m, n - m, result)
    item.pop()# m 不在集合当中
    find_combine(item, m-1, n, result)



class Solution(object):

    def solve(self,m,n):
        item = []
        result = []

        find_combine(item,m,n,result)
        count = len(result)
        return count

# print(Solution().solve(5,5))
class Solution(object):
    def solve(self,n):
        Num2P = [0,1,5,-1,-1,2,9,-1,8,6]
        count = 0
        for i in range(1,n+1):
            s = str(i)
            length = len(s)
            new_num = ''
            flag = 1
            for j in range(length):
                letter = int(s[j])
                old2new = Num2P[int(letter)]
                if old2new==-1:
                    flag = -1
                    break
                new_num = new_num + str(old2new)
            if flag == 1 and int(new_num) != i:
                count = count+1
        return count

print(Solution().solve(10000))
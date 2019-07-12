## 题目

##### 灵犀编程比赛题目

#### 练习BY张嘉玮

* ### 第一题

  题目：

  ```markdown
  题目：保留2位小数
  描述：给定字符串类型的浮点数（即可使用float()函数转为浮点数），返回其带有两位小数的浮点数，并转为字符串类型返回
  输入数据范围：对应的浮点数绝对值小于 10000
  样例输入和输出：
  '5' -> '5.00'
  '1.0' -> '1.00'
  '1.555' -> '1.55'
  '9.991' -> '9.99'
  
  示例代码：
  # 上传的代码文件中必须包含 Solution 类和 solve 函数，允许有其他类和其他函数
  class Solution(object):
      def solve(self, s):
          """
          :type s: str
          :rtype str
          """
  ```

  解答：

  ```python
  
  
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
  
  ```

* ### 第二题

  题目：

  ```python
  题目：博览群书
  描述：公司的读书群里有很多同学，小灵每个月会统计每本书的阅读人员，评选出读书最多的同学，予以奖励。
        这个月大家读书非常积极，小灵统计得头晕脑胀，你能帮TA快速统计出结果吗
        输入格式为 [nums1, nums2, nums3...]，其中nums(i) 表示读第完i本书的同学id列表
        输出格式为读书最多的同学列表，如有多位同学，返回列表请按id进行排序
        
  样例输入1：[[1, 2], [2, 3]]，期望输出：[2]
  解释1：读完第一本书有1、2这两位同学，读完第二本书的是2、3两位同学，同学2读书最多
  
  样例输入2：[[1, 2, 3], [2, 3, 4]]，期望输出：[2, 3]
  解释2：读完第一本书有1、2、3三位同学，读完第二本书的是2、3、4三位同学，同学2和同学3读书最多
  
  示例代码：
  # 上传的代码文件中必须包含 Solution 类和 solve 函数，允许有其他类和其他函数
  class Solution(object):
      def solve(self, nums_list):
          """
          :type nums_list: list[list[int]]
          :rtype list[int]
          """
  ```

  解答：

  ```python
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
  
  ```

  

* ### 第三题

  题目：

  ```python
  题目：神奇数字
  描述：如果一个整数在每个数字都单独旋转180度后，还能保持是一个有效的整数，且与原来的整数不同，我们称这样的整数是一个神奇的数字
        数字0、1、8在旋转180度后仍然为数字，且保持不变
        数字2和5可以相互旋转
        数字6和9可以相互旋转
        给定一个整数N，请找出从1到N有多少个神奇数字
  输入范围：1 <= N <= 10000     
  样例输入：12，期望输出：5
  在[1, 12]范围内有五个好数字：2、5、6、9、12
  
  class Solution(object):
      def solve(self, n):
          """
          :type n: int
          :rtype int
          """
  ```

  解答：

  ```python
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
  ```

  

* ### 第四题

  题目：

  ```python
  题目：超级加加加
  描述：有1,2,3...m一共m个正整数，返回和为n的所有组合的个数，每个数最多可以用两遍
  
  样例输入：m=5, n=5
  期望输出：5
  解释：可能加法组合有5=5、5=1+4、5=2+3、5=1+1+3、5=1+2+2共五种情况
  
  class Solution(object):
      def solve(self, m, n):
          """
          :type m: int
          :type n: int
          :rtype int
          """
  ```

  解答：

  ```python
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
  ```

  

* ### 第五题

  题目：

  ```python
  题目：范围最大值
  描述：给定一个数组和范围长度，找出连续范围内最大的数
  数据范围：数组长度 < 5000，范围长度小于5000
  
  样例输入：[1, 0, -3, 5, -1, 0, 7, 3], 3
  期望输出：[1, 5, 5, 5, 7, 7]
  范围（用中括号标出）          最大值
  ----------------------       -----
  [1  0  -3] 5  -1  0  7  3      1  
   1 [0  -3  5] -1  0  7  3      5
   1  0 [-3  5  -1] 0  7  3      5
   1  0  -3 [5  -1  0] 7  3      5
   1  0  -3  5 [-1  0  7] 3      7
   1  0  -3  5  -1 [0  7  3]     7
  
  class Solution(object):
      def solve(self, nums, n):
          """
          :type nums: list[int]
          :type n: int
          :rtype list[int]
          """
  ```

  解答：

  ```python
  class Solution(object):
      def solve(self,nums,n):
          if len(nums)<n:
              return []
          res = []
          for i in range(len(nums)-n+1):
              res.append(max(nums[i:i+n]))
  
          return res
  ```

  


# NEETCODE concept:
# The idea is to multiply numbers before(pre) that number, and after(post) that number
# Make 2 arrays, pre and post. We'll be populating pre array with product of numbers before nums[i] and post array with product of numbers after nums[i]
# example- nums = |  2  |  5  |  1  |  3  |
# there is nothing before 2, so pre[0] = 1, there is only 2 before 5, so pre[1] = 2, there are 2, 5 before 1, so product of numbers before 1 pre[2] = 10, pre[3] = 10
# pre = |  1  |  2  |  10  |  10  |
# there is nothing after 3, so post[3] = 1- but populating in reverse isn't possible, so I'll populate from left to right, and then reverse the array. So post[0] = 1
# after 1, there is 3, so post[1] = 3, after 5 there is 1, 3, so product of numbers after 5 = post[2] = 3, post[3] = 15
# post = |  1  |  3  |  3  |  15  |
# post[::-1] = |  15  |  3  |  3  |  1  |
# Now multiple values from both arrays that are at the same index. This is the final answer.

# TC = O(n) (iterating through array thrice in linear time,  n + n + n = 3n ~ n)
# SC = O(n) (pre = n, post = n, post[::-1] = n, n + n + n = 3n ~ n)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
      pre = [1]
      post = [1]
      
      res = []
      
      pre_prod = 1
      post_prod = 1
      
      for i in range(len(nums)-1):
        pre_prod *= nums[i]
        pre.append(pre_prod)
        
      for j in range(len(nums)-1, 0, -1):
        post_prod *= nums[j]
        post.append(post_prod)
        
      post = post[::-1]
      
      for k in range(len(nums)):
        res.append(pre[k] * post[k])
        
      return res
      
-----------------------------------------------------------------------------------------------------------------------------------------------------------------      




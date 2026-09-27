class Solution(object):
    def threeSumClosest(self, nums, target):
       nums.sort() 
       closest_sum=float('inf')
       for i in range(len(nums)):
           left=i+1
           right=len(nums)-1
           while left<right:
                 sums=nums[i]+nums[left]+nums[right]
                 if sums==target:
                    return sums
                 elif abs(sums-target)<abs(closest_sum-target):
                      closest_sum=sums
                 if  sums<target:
                    left+=1
                 else:
                    right-=1 
       return closest_sum               
                 

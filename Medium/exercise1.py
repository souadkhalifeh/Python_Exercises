# Exercise 1
# Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.
# Input : [-1,0,1,2,-1,-4] 
# Output : [[-1, -1, 2], [-1, 0, 1]] 
# Note : Find the unique triplets in the array.

def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i>0 and nums[i]== nums[i - 1]:
            continue
        left=i+1
        right=len(nums) - 1
        while left<right: 
            total=nums[i]+nums[left]+nums[right]
            
            if total==0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1    
            elif total<0:
                left+=1
            else:
                right-=1        
    return result            
                
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))                
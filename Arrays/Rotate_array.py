#Question: Roitate array by k elements
# Time Complexity: O(n)
#Space Complexity: O(n)

nums = [1,2,3,4,5,6,7]
k = 3

n = len(nums)
temp = [0] * n

for i in range(n):
    temp[(i + k) % n] = nums[i]
nums[0:n] = temp
print(nums)

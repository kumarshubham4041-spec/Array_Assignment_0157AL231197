# Question :Find sum of elements in an array
# Time Complexity : O(n)
# Space Complexity: O(1)

arr = [1, 2, 3, 4]
total= 0

for i in range(len(arr)):
    total += arr[i]

print(total)

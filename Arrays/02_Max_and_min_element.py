#Question: Find min and max element in an array
#Time  Complexity : O(n)
#Space Complexity: O(1)

arr = [ 5,60,6,1,56,88,3]
max = float('-inf')
min = float('inf')
for num in arr:
    if num>max:
        max= num
    if num<min:
        min = num
print("Maximum element: ", max)
print("Minimum element: ", min)

# Question: Fidn second largest element in an array
#Time Complexity: O(n)
#Space Complexity: O(1)
arr = [12, 35, 1, 10, 34, 1]
n= len(arr)
larg= -1
ans = -1
for i in range(n):
    if arr[i]>larg:
        ans= larg
        larg= arr[i]
    elif arr[i]!=larg and arr[i]>ans:
        ans=arr[i]
print(ans)

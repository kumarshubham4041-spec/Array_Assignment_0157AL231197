#Question: Reverse an aray
#Approach: Two pointers approach
#Time Complexity : O(n)
#Space Complexity : O(1)

arr = [1,4,5,6,7,8]
n = len(arr)-1
start = 0
end = n
while start<end:
    temp = arr[start]
    arr[start]= arr[end]
    arr[end]= temp
    start+=1
    end -= 1
print (arr)

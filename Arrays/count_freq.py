#Question: Count frequrency of elements in an array
#Time complexity :O(n)
# Space Complexity: O(n)

arr = [1, 2, 2, 3, 3, 5]
freq = {}
ans=[]       
for nums in arr:
    freq[nums]= freq.get(nums,0)+1

    for i,j in freq.items():
        ans.append([i,j])
            
print(ans)

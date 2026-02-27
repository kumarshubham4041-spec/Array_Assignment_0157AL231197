# Question: Find leader element from given which are greater than all elements on its rightmost.
# Time Complexity: O(n)
# Space Complexity : O(n)

def leaders(self, arr):
        # code here
        leaders = []
        n = len(arr)
        
        max_right= arr[n-1]
        leaders.append(max_right)
        for i in range (n-2,-1,-1):
            if arr[i]>= max_right:
                leaders.append(arr[i])
                max_right= arr[i]
                
        leaders.reverse()
        return leaders

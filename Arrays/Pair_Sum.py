nums = [2,7,11,15]
target = 9
index_map = {}
for i in range(len(nums)):
    complement = target - nums[i]
    if complement in index_map :
        print([ index_map[complement], i])
            
    index_map[nums[i]] = i
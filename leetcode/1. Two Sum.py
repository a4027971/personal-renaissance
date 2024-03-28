'''
1 
time: O(N^2)
space: O(N)
tag: Array

2
time: O(N)
space: O(N) + O(2N) = O(N)
tag: Hash Table

# TODO:
# 1 optimize
# 2 read others answer
'''

# 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        numberSize = len(nums)
        for i in range(0, numberSize):
            for j in range(i+1, numberSize):
                if nums[i] + nums[j] == target:
                  ans = [i, j]  
                  break
        
        if len(ans) == 0:
            raise Exception('no answer')

        return ans

# 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keymap = {}
        ans = []

        for seq in range(0, len(nums)):
            sub = target - nums[seq]
            if sub in keymap:
                ans = [keymap[sub], seq]
                break
            elif nums[seq] not in keymap:
                keymap[nums[seq]] = seq

        if len(ans) == 0:
            raise Exception("no answer")  

        return ans
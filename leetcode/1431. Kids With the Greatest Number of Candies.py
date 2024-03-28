'''
time: O(N)
space: O(N)

# TODO:
# 1 optimize
# 2 read others answer
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy_num = max(candies)
        ans = []

        for i in range(len(candies)):
            ans.append(candies[i]+extraCandies >= max_candy_num)
        
        return ans
        
        
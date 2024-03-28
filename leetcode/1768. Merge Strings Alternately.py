'''
time: O(N+M)
space: O(N+M)
tag: Array, String

# TODO:
# 1 optimize
# 2 read others answer
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        len1 = len(word1)
        len2 = len(word2)
        len_sum = len1 + len2
        cur1 = 0
        cur2 = 0
        ans = ""

        while len_sum > cur1+cur2:
            if cur1 < len1:
                ans += word1[cur1]
                cur1 += 1
            
            if cur2 < len2:
                ans += word2[cur2]
                cur2 += 1
            
        return ans

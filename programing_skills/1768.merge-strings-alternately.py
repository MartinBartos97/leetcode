#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        min_len = min(l1, l2)
        str_merge = str()
        for i in range(0,min_len):
            str_merge = str_merge + word1[i]
            str_merge = str_merge + word2[i]
        str_merge = str_merge + word1[min_len:]
        str_merge = str_merge + word2[min_len:]
        return str_merge
# @lc code=end

#join method 

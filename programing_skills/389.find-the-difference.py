#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        checked = str()
        for i in t:
            s_count = s.count(i)
            if s_count != t.count(i)and i not in checked:
                return i
            else:
                checked.join(i)
                continue

# @lc code=end
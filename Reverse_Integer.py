# Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:
# Input: 123
# Output: 321
# Example 2:
# Input: -123
# Output: -321
# Example 3:
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within
# the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        v = abs(x) # 带符号数 // 和 % 会与预期不同 所以取绝对值
        sign_flag = 1 if x >= 0 else -1
        while v:
            res, v = res * 10 + v % 10, v // 10
        ret = res * sign_flag
        if  ret > 2**31 - 1 or ret < -2**31:
            return 0
        return ret
# Leetcode # 67
# Given two binary strings, return their sum(also a binary string).
# The input strings are both non - empty and contains only characters
# 1 or 0.
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a, len_b = len(a), len(b)
        num_dict = {'0': 0, '1': 1}
        i = -1
        if len_a > len_b:
            long_num, short_num = a, b
            max_len, min_len = len_a, len_b
        else:
            long_num, short_num = b, a
            max_len, min_len = len_b, len_a
        res = []
        carry_val = 0
        while i >= -max_len:
            if i >= -min_len:
                num_val = (num_dict[long_num[i]] ^ num_dict[short_num[i]] ^ carry_val)
                carry_val = (num_dict[long_num[i]] & carry_val) | (num_dict[short_num[i]] & carry_val) | (
                            num_dict[long_num[i]] & num_dict[short_num[i]])
                res.append(str(num_val))
            else:
                num_val = (num_dict[long_num[i]] ^ carry_val)
                carry_val = (num_dict[long_num[i]] & carry_val)
                res.append(str(num_val))
            i -= 1
        else:
            if carry_val:
                res.append(str(carry_val))
        res.reverse()
        return ''.join(res)

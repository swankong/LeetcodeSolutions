# Longest substring without repeating characters
# Given a string, find the length of the longest substring without repeating characters.
# Example 1:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring_1(self, s):  # Solution 1
        """
        :type s: str
        :rtype: int
        """
        str_length = len(s)
        max_len = 0
        if str_length > 0:  # return if input string is empty. 空字串直接返回
            for i in range(str_length):
                stat_list = []
                for j, c in enumerate(s[i:]):
                    if c in stat_list:
                        j -= 1  # get repeat string, move back. 找到重复字符，退一格
                        break
                    else:
                        stat_list.append(c)
                if max_len < j + 1:  # 最大值
                    max_len = j + 1
            return max_len
        else:
            return 0

    def lengthOfLongestSubstring_2(self, s):

        str_len = len(s)  # string length
        if str_len <= 1:  # return empty or 1 element list
            return str_len

        str_map = dict() # hash map for replicated element
        max_len, i = 0, 0
        while i < str_len:
            sub_len = 0
            for j, c in enumerate(s[i:]):
                if str_map.get(c) is None:
                    str_map[c] = j + i
                    sub_len += 1
                else:
                    max_len = max(max_len, sub_len)
                    i = str_map[c] + 1
                    str_map.clear()
                    break
            else:
                i += 1
            max_len = max(max_len, sub_len)
        return max_len


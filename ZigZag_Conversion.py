# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n_rows = numRows
        rst_list = []  # temp results in a 2-d list. 二维列表起始
        s_len = len(s)
        if s_len <= 1 or n_rows <= 1:  # some special cases. 边界情况
            return s
        for i in range(0, n_rows):  # Process by line. 按行处理
            rst_list.append([])  # A new line. 每次新创建一行
            if i == 0 or i == n_rows - 1:  # From top to bottom, sample by 2x(n_rows - 1) 顶部和底部，取样间隔都是2*(n_rows-1)
                rst_list[i].extend(s[i:s_len:2 * (n_rows - 1)])  # 直接切片取样，NOTE:切片会临时复制一个对象
            else:
                for j in range(i, s_len, 2 * (n_rows - 1)):  # 其余行都是按照 2*(n_rows-1)步长取样，但偏移不同
                    rst_list[i].append(s[j])  # insert first char. 首字符加入
                    if j + 2 * (n_rows - 1) - 2 * i < s_len:  # 首字符 + 取样偏移 - 2*i 就是第二字符
                        rst_list[i].append(s[j + 2 * (n_rows - 1) - 2 * i])

        return ''.join([''.join(x) for x in rst_list])  # merge to a string with join method. 二维列表变成一维字符串
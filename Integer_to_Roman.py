# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.
# Example 1:
# Input: 3
# Output: "III"
# Example 2:
# Input: 4
# Output: "IV"
# Example 3:
# Input: 9
# Output: "IX"


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if 1 <= num <= 3999:
            n_kilo = num // 1000
            n_perc = (num % 1000) // 100
            n_deci = (num % 100) // 10
            n_digi = num % 10
            kilo_str = 'M' * n_kilo
            perc_str = self.makePercent(n_perc)
            deci_str = self.makeDecimal(n_deci)
            digi_str = self.makeDigital(n_digi)
            return ''.join([kilo_str, perc_str, deci_str, digi_str])
        else:
            return None

    def makePercent(self, n):
        rome_str = ''
        if 0 < n < 4:
            rome_str = 'C' * n
        elif 4 <= n <= 5:
            rome_str = ''.join(['C' * (5 - n), 'D'])
        elif 5 < n < 9:
            rome_str = ''.join(['D', 'C' * (n - 5)])
        elif n == 9:
            rome_str = 'CM'
        return rome_str

    def makeDecimal(self, n):
        rome_str = ''

        if 0 < n < 4:
            rome_str = 'X' * n
        elif 4 <= n <= 5:
            rome_str = ''.join(['X' * (5 - n), 'L'])
        elif 5 < n < 9:
            rome_str = ''.join(['L', 'X' * (n - 5)])
        elif n == 9:
            rome_str = 'XC'
        return rome_str

    def makeDigital(self, n):
        rome_str = ''
        if 0 < n < 4:
            rome_str = 'I' * n
        elif 4 <= n <= 5:
            rome_str = ''.join(['I' * (5 - n), 'V'])
        elif 5 < n < 9:
            rome_str = ''.join(['V', 'I' * (n - 5)])
        elif n == 9:
            rome_str = 'IX'
        return rome_str
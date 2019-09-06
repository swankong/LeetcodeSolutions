class Solution:
    def plusOne(self, digits):
        carry_val = 0   # carry number 进位
        n_digits = len(digits)  # length 长度
        for i in range(n_digits, 0, -1):
            if i == n_digits:
                sum_val = digits[i - 1] + 1
            else:
                sum_val = digits[i - 1] + carry_val
            quo_val = sum_val % 10
            carry_val = sum_val // 10
            digits[i - 1] = quo_val
            if not carry_val:
                break
        else:
            if carry_val:
                digits.insert(0, carry_val)  # If the carry is not zero after the loop.
        return digits
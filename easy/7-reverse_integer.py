class Solution:
    def reverse(self, x: int) -> int:

        result = 0

        # whether number is negative or not
        is_number_negative = False
        if x < 0:
            is_number_negative = True

        # we run our logic only on absolute value
        abs_number = abs(x)

        while abs_number > 0:
            num_to_add = abs_number % 10
            abs_number = int(abs_number / 10)
            result = result * 10 + num_to_add

            # if the result goes out of bound for 32 bit integer result should be 0
            # This is mentioned explicitly int the problem statement
            if result < -2 ** 31 or result > 2 ** 31 - 1:
                result = 0
                break

        if is_number_negative:
            return -result
        else:
            return result




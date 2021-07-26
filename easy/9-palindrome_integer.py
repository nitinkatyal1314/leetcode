class Solution:

    def isPalindrome(self, x: int) -> bool:
        num_to_str = str(x)
        is_palindrome = True

        left = 0
        right = len(num_to_str) - 1

        while left < right:
            if num_to_str[left] == num_to_str[right]:
                left += 1
                right -= 1
                continue
            else:
                is_palindrome = False
                break

        return is_palindrome

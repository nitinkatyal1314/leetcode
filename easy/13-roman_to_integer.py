class Solution:
    def romanToInt(self, s: str) -> int:

        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        num = 0
        num += mapping[s[len(s) - 1]]
        curr = len(s) - 2

        while curr >= 0:

            if mapping[s[curr]] >= mapping[s[curr + 1]]:
                num += mapping[s[curr]]
            else:
                num -= mapping[s[curr]]

            curr -= 1

        return num

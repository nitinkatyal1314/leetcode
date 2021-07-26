class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        sorted_items = sorted(strs, key=lambda s: len(s))

        smallest_string = sorted_items[0]

        # print(" Smallest : ",smallest_string )

        for word in sorted_items[1:]:
            # print("Comparing with ", word)
            for i in range(0, len(smallest_string)):

                # print(" matching character : ", smallest_string[i], word[i])

                if word[i] == smallest_string[i]:
                    continue
                else:
                    smallest_string = smallest_string[: i]
                    break

            # print(" smallest string updated to : ", smallest_string)

            if len(smallest_string) == 0:
                break

        return smallest_string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        start_index = 0
        end_index = 1
        largest = 0
        curr_s = s[start_index]
        while largest < (len(s) - start_index) and end_index != len(s):
            if s[end_index] not in curr_s:
                curr_s += s[end_index]
                end_index += 1
            else:
                largest = max(len(curr_s), largest)
                start_index += 1
                end_index = start_index+1
                curr_s = s[start_index]

        largest = max(len(curr_s), largest)

        return largest
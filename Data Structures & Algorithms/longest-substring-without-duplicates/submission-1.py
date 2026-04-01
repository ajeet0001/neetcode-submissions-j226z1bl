class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        char_dict = {}
        ans = 0
        for right, char in enumerate(s):
            # if duplicate occure in current window
            if char in char_dict and char_dict[char]>=left:
                left = char_dict[char]+1
            char_dict[char] = right
            ans = max(ans,right-left+1)
        return ans
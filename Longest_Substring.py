class Solution(object):
    def LengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
### Solution 1: Sliding Window
        left = 0
        right = 0
        max_length = 0
        seen = {}

        while right < len(s):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1

            seen[s[right]] = right
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length

s = Solution()
print(s.LengthOfLongestSubstring("abcabcbb"))  # Output: 3

### Solution 2: Brute Force
#         s = [char for char in s]
#         current_length = 0
#         max_length = 0
#         l = []
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if s[j] not in l:
#                     l.append(s[j])
#                     current_length += 1
#                 else:
#                     if current_length > max_length:
#                         max_length = current_length
#                     current_length = 0
#                     l = []
#         return max_length


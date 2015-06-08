class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        prev_map = self.prev_map(s)
        max_length = 0
        start = 0
        for i, c in enumerate(s):
            prev = prev_map[i]
            if prev >= start:
                start = prev + 1
            max_length = max(max_length, i - start + 1)
        return max_length

    @staticmethod
    def prev_map(s):
        """
        Generate the previous character position map.
        For example: "abcabcbb" -> [None, None, None, 0, 1, 2, 4, 6]
        """
        prev_map = []
        char_map = {}
        for i, c in enumerate(s):
            prev = char_map.get(c)
            char_map[c] = i
            prev_map.append(prev)
        return prev_map

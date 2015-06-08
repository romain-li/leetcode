class Solution:
    SEPARATOR = '#'

    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        """ manacher algorithm """
        pre_s = self.pre_process(s)
        length = len(pre_s)
        p = [0] * length
        mx = 0
        pi = 1
        max_length = 0
        max_length_position = 0
        for i in xrange(1, length - 1):
            offset = min(mx - i, p[2 * pi - i]) if mx > i else 1
            p[i] = self.palindrome_length(pre_s, length, i, offset)
            if p[i] > max_length:
                max_length = p[i]
                max_length_position = i
            if i + p[i] > mx:
                mx = i + p[i]
                pi = i
        return pre_s[max_length_position - max_length:max_length_position + max_length].replace(self.SEPARATOR, '')

    @classmethod
    def pre_process(cls, s):
        return cls.SEPARATOR + cls.SEPARATOR.join(s) + cls.SEPARATOR

    @classmethod
    def palindrome_length(cls, s, length, half, offset=1):
        while cls.inbound(half, offset, length) and s[half - offset] == s[half + offset]:
            offset += 1
        return offset - 1

    @classmethod
    def inbound(cls, half, offset, length):
        return half - offset >= 0 and half + offset < length

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        length_a = len(A)
        length_b = len(B)
        median_index = (length_a + length_b - 1) / 2

        a1 = 0
        a2 = length_a - 1
        b1 = 0
        b2 = length_b - 1

        while (a1 != a2 and b1 != b2):
            a_half = (a1 + a2) / 2
            b_half = (b1 + b2) / 2

            if (A[a_half] < B[b_half]):
                if (a_half + b_half) < median_index:
                    a1 = a_half if a1 != a_half else a2
                else:
                    b2 = b_half
            else:
                if (a_half + b_half) < median_index:
                    b1 = b_half if b1 != b_half else b2
                else:
                    a2 = a_half

        def _findMedian(a, B, index):
            print a, B, index
            if B[index] < a:
                return B[index]
            else:
                return a

        if (a1 == a2):
            return _findMedian(A[a1], B, median_index - a1)
        else:
            return _findMedian(B[b1], A, median_index - b1)


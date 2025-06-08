import unittest

# 探索の再帰関数
def dfsum(pos, sum_curr, sum_dst, X):
    if sum_curr == sum_dst:
        return True
    if pos == len(X):
        return False
    if dfsum(pos + 1, sum_curr, sum_dst, X):
        return True
    if dfsum(pos + 1, sum_curr + X[pos], sum_dst, X):
        return True
    return False

def solution(sum_dst, X):
    if dfsum(0, 0, sum_dst, X):
        return True
    else:
        return False

class TestSolution(unittest.TestCase):
    def test_1_sample(self):
        self.assertEqual(solution(13, [1, 2, 4, 7]), True)

    def test_2_sample(self):
        self.assertEqual(solution(23, [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]), True)
    

unittest.main(argv=['first-arg-is-ignored'], exit=False)
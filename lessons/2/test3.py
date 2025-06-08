import unittest
import os

dir_current = os.path.dirname(__file__)

# テキスト読み込んでリスト化
def read_input(path_txt):
    arr_out = []
    with open(path_txt) as f:
        lines = f.readlines()
    arr_out = [[char for char in line.strip()] for line in lines]
    return arr_out

# 池のWを"."に変換
def over_lake(array_target, x, y):
    if array_target[x][y] == "W":
        array_target[x][y] = "."
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < len(array_target) and 0 <= y + j < len(array_target[0]):
                    over_lake(array_target, x + i, y + j)
    return array_target

# 池カウント
def solution():
    array_target = read_input(dir_current + "/datas/2_input.txt")
    len_vertical = len(array_target)
    len_horizontal = len(array_target[0])
    count_lake = 0
    for i in range(len_vertical):
        for j in range(len_horizontal):
            if array_target[i][j] == "W":
                over_lake(array_target, i, j)
                count_lake += 1
    return count_lake


class TestSolution(unittest.TestCase):
    def test_1_sample(self):
        self.assertEqual(solution(), 4)
    

unittest.main(argv=['first-arg-is-ignored'], exit=False)
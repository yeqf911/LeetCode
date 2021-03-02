from typing import List

from leezy import solution, Solution


class Q566(Solution):
    @solution
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0])

        if r * c != row * col or (r == row and c == col):
            return nums

        new_nums = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                new_nums[i][j] = nums[i][j]

        return new_nums


def main():
    q = Q566()
    q.add_case(q.case([[1, 2], [3, 4]], 4, 1))
    q.add_case(q.case([[1, 2], [3, 4]], 1, 4))
    q.run()


if __name__ == '__main__':
    main()

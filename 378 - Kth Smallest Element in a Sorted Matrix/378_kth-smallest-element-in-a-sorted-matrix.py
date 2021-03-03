from typing import List

from leezy import solution, Solution


class Q378(Solution):
    @solution
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])

        smallest = matrix[0][0]
        biggest = matrix[row - 1][col - 1]
        mid = (smallest + biggest) / 2


def main():
    q = Q378()
    q.add_case(q.case([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
    q.run()


if __name__ == '__main__':
    main()

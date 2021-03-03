from typing import List

from leezy import solution, Solution


class Q240(Solution):
    @solution
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row = len(matrix)
        col = len(matrix[0])

        r_idx = 0
        c_idx = col - 1
        result = False

        while r_idx < row and c_idx >= 0:
            cur = matrix[r_idx][c_idx]
            if cur == target:
                result = True
                break
            if cur < target:
                r_idx += 1
            else:
                c_idx -= 1

        return result

    @solution
    def searchMatrix2(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False


def main():
    q = Q240()
    q.add_case(
        q.case([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
               5))
    q.add_case(q.case([[-1, 3]], 3).assert_equal(True))
    q.run()


if __name__ == '__main__':
    main()

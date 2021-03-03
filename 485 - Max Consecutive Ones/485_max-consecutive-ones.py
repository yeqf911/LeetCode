from typing import List

from leezy import solution, Solution


class Q485(Solution):
    @solution
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0

        for i in nums:
            count = 0 if i == 0 else count + 1
            max_count = max(count, max_count)

        return max_count


def main():
    q = Q485()
    q.add_case(q.case([1, 0, 1, 1, 0, 1]))
    q.run()


if __name__ == '__main__':
    main()

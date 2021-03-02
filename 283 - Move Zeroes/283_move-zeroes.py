from typing import List

from leezy import solution, Solution


class Q283(Solution):
    @solution
    def moveZeroes(self, nums: List[int]):
        index = 0
        for n in nums:
            if n != 0:
                nums[index] = n
                index += 1

        for i in range(index, len(nums)):
            nums[index] = 0
            index += 1
        return nums

    @solution
    def moveZeroes2(self, nums: List[int]):
        n = len(nums)
        right = left = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums


def main():
    q = Q283()
    q.add_case(q.case([0, 1, 0, 3, 12]))
    q.run()


if __name__ == '__main__':
    main()

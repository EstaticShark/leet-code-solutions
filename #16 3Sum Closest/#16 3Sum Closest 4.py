from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    closest_sum = nums[0] + nums[1] + nums[2]
    nums.sort()
    min_diff = abs(target - closest_sum)

    for pivot in range(nums.__len__() - 2):
        j = pivot + 1
        k = nums.__len__() - 1

        while j != k:
            sum = nums[pivot] + nums[j] + nums[k]
            if sum < target:
                j += 1
            elif sum == target:
                return sum
            else:
                k -= 1

            if abs(target - sum) < min_diff:
                closest_sum = sum
                min_diff = abs(target - closest_sum)

    return closest_sum


if __name__ == '__main__':
    print(threeSumClosest([-1, 2, 1, -4], 1))
    print(threeSumClosest([-1, -5, -3, -4, 2, -2], 0))
    print(threeSumClosest([-3, -2, -5, 3, -4], 1))
    print(threeSumClosest([-5, -4, -3, -2, 3], 1))
    print(threeSumClosest([1, 1, 1, 1, 1], 0))
    print("bye")
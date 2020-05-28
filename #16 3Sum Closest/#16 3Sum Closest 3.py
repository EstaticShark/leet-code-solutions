from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    closest_sum = nums[0] + nums[1] + nums[2]
    items = nums.__len__()
    nums.sort()

    for pivot in range(items - 2):
        j = pivot + 1
        k = items - 1

        while j != k:
            sum = nums[pivot] + nums[j] + nums[k]
            if sum < target:
                j += 1
            elif sum == target:
                return sum
            else:
                k -= 1

            if abs(target - sum) < abs(target - closest_sum):
                closest_sum = sum

        pivot += 1

    return closest_sum


if __name__ == '__main__':
    print(threeSumClosest([-1, 2, 1, -4], 1))
    print(threeSumClosest([-1, -5, -3, -4, 2, -2], 0))
    print(threeSumClosest([-3, -2, -5, 3, -4], 1))
    print(threeSumClosest([-5, -4, -3, -2, 3], 1))
    print(threeSumClosest([1, 1, 1, 1, 1], 0))
    print("bye")
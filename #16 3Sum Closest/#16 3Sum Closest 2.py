from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    pivot = 0
    min_diff = target - (nums[0] + nums[1] + nums[2])
    items = nums.__len__()
    nums.sort()

    while pivot < (items - 2):
        j = pivot + 1
        k = items - 1
        p_target = target - nums[pivot]

        while j != k:
            if abs(p_target - (nums[j] + nums[k])) < abs(min_diff):
                min_diff = p_target - (nums[j] + nums[k])
                if min_diff == 0:
                    return target
            if j != k - 1 :
                if abs(p_target - (nums[j + 1] + nums[k])) < abs(p_target - (nums[j] + nums[k - 1])):
                    j += 1
                else:
                    k -= 1
            else:
                j += 1

        pivot += 1

    return target - min_diff


if __name__ == '__main__':
    #print(threeSumClosest([-1, 2, 1, -4], 1))
    print(threeSumClosest([-1, -5, -3, -4, 2, -2], 0))
    #print(threeSumClosest([-3, -2, -5, 3, -4], 1))
    #print(threeSumClosest([-5, -4, -3, -2, 3], 1))
    #print(threeSumClosest([1, 1, 1, 1, 1], 0))
    print("bye")
from typing import List

def maxArea(height: List[int]) -> int:
    j,k = 0, height.__len__() - 1
    max_area = 0

    while j < k:
        if (k - j)*(min(height[j], height[k])) > max_area:
            max_area = (k - j)*(min(height[j], height[k]))
        if height[j] < height[k]:
            j += 1
        else:
            k -= 1

    return max_area

if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]))
    print("bye")
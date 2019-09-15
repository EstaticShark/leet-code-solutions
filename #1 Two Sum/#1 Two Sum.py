from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        ###
        There should be more ways of completing this other than going through every number and adding them together.
        Brute forcing this would not be as fun.

        Ideas:
        #Brute Force: would take O(n^2) at most, where the starting indice would increase and take 1 less time
        than the last indice

        #List of numbers: subtract each number to the target and store the difference in a list, you could then use
        the indice that the number was on inside the list and use the in operator to find the answer.
        ###
        """
        diff_num = []

        for item in nums:
            diff_num.append(target - item)

        for i in range(len(nums)):
            num_index = -1
            search_index = 0
            searched = False

            while not searched:
                try:
                    num_index = diff_num.index(nums[i], search_index)
                except ValueError:
                    num_index = -1

                if num_index == i:
                    # If the indices are the same
                    search_index += 1

                elif num_index == -1:
                    # If the number is not found
                    searched = True

                else:
                    # If the number is found and isn't the same indice
                    return [i, num_index]

        return []




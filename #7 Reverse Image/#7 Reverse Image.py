class Solution:
    def reverse(self, x: int) -> int:
        if x > 2 ** 31 - 1 or x < -1 * (2 ** 31):
            return 0

        str_x = str(x)[::-1]

        if "-" in str_x:
            if int(str(-1 * x)[::-1]) * -1 >= -1 * (2 ** 31):
                return int(str(-1 * x)[::-1]) * -1
            return 0

        if int(str_x) <= 2 ** 31 - 1:
            return int(str(x)[::-1])
        return 0
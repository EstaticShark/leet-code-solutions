class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zig_string = ""
        row_string = []
        row_i = 0
        counter = 0
        down = True

        for i in range(numRows):
            row_string.append("")

        while counter < len(s):
            row_string[row_i] += s[counter]
            counter += 1
            if down:
                if row_i == numRows - 1:
                    down = False
                    row_i -= 1
                else:
                    row_i += 1
            else:
                if row_i == 0:
                    down = True
                    row_i += 1
                else:
                    row_i -= 1

        for item in row_string:
            zig_string += item

        return zig_string
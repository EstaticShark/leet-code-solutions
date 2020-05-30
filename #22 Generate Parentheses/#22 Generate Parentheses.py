from typing import List

def generateParenthesis(n: int) -> List[str]:
    if n == 0:
        return []

    output = []

    """
    # Failed attempt here, too slow. I realized that its better to work from the
    # outside that it is to work from the inside, since working from inside does
    # not allow multiple nested solutions
    def backtrack(curr, left):
        if left == n:
            if curr not in output:
                output.append(curr)
        elif left < n:
            backtrack('(' + curr + ')', left + 1)
            backtrack(curr + '()', left + 1)
            backtrack('()' + curr, left + 1)
            if left != 0:
                backtrack(curr + curr, left*2)

    backtrack("", 0)
    """
    def backtrack(curr, left, right):
        if curr.__len__() == 2*n:
            output.append(curr)
        else:
            if left < n:
                backtrack(curr + "(", left + 1, right)
            if right < left:
                backtrack(curr + ")", left, right + 1)

    backtrack("", 0, 0)

    return output

if __name__ == '__main__':
    print(generateParenthesis(1))
    print(generateParenthesis(2))
    print(generateParenthesis(3))
    print(generateParenthesis(4))
    print(generateParenthesis(5))
    print("bye")

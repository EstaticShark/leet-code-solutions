from typing import List

def isValid(s: str) -> bool:
    p_index = {'(' : 0 ,')' : 3, '{' : 1 ,'}' : 4, '[' : 2 ,']' : 5}
    backlog = []
    count = 0
    last_added = -1

    for item in s:
        if p_index[item] < 3:
            backlog.append(item)
            count += 1
            last_added = p_index[item]
        else:
            if p_index[item] == last_added + 3:
                backlog.pop(count - 1)
                count -= 1
                if count != 0:
                    last_added = p_index[backlog[count - 1]]
                else:
                    last_added = -1
            else:
                return False

    if count == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(isValid("()"))
    print(isValid("())"))
    print(isValid("(()"))
    print(isValid("(}"))
    print(isValid("()[]{}"))
    print(isValid("({}[])[{[()()[]]}]{}"))
    print(isValid("({)[]{}}"))
    print(isValid("()[{}]"))

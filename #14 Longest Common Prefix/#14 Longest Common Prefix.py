
def longestCommonPrefix(strs) -> str:
    if strs.__len__() == 0:
        return ""

    prefix = ""
    current_letter = 0
    smallest_length = min(strs, key=len).__len__()

    while current_letter < smallest_length:
        prefix += strs[0][current_letter]
        for i in range(1, strs.__len__()):
            if strs[i][current_letter] != prefix[-1]:
                prefix = prefix[:-1]
                return prefix
        current_letter += 1

    return prefix

if __name__ == "__main__":
    print(longestCommonPrefix(["flow", "floor", "flop"]))
    print(longestCommonPrefix(["flow", "floor", "dlop"]))
    print(longestCommonPrefix(["flow", "dloor", "flop"]))
    print(longestCommonPrefix(["fff", "ff", "ff"]))
    print(longestCommonPrefix([]))
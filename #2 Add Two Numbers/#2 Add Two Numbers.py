# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num_list1 = []
        num_list2 = []
        curr1 = l1
        curr2 = l2

        while curr1 != None:
            num_list1.append(curr1.val)
            curr1 = curr1.next

        while curr2 != None:
            num_list2.append(curr2.val)
            curr2 = curr2.next

        num1 = 0
        for i in range(len(num_list1)):
            num1 += (num_list1[i]) * (10 ** (i))

        num2 = 0
        for j in range(len(num_list2)):
            num2 += (num_list2[j]) * (10 ** (j))

        sum_num = num1 + num2

        return_node = ListNode(0)
        curr_node = return_node

        for k in range(len(str(sum_num))):
            curr_node.val = str(sum_num)[::-1][k]

            if k < len(str(sum_num)) - 1:
                curr_node.next = ListNode(0)
                curr_node = curr_node.next

        return return_node


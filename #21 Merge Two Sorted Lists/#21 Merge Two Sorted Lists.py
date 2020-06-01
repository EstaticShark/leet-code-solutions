class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None and l2 == None:
        return None
    elif l1 == None:
        return l2
    elif l2 == None:
        return l1

    if l1.val < l2.val:
        first = l1
        l1 = l1.next
    else:
        first = l2
        l2 = l2.next

    curr_node = first

    while l1 != None and l2 != None:
        if l1.val <= l2.val:
            curr_node.next = l1
            l1 = l1.next
        else:
            curr_node.next = l2
            l2 = l2.next

        curr_node = curr_node.next

    if l1 == None:
        curr_node.next = l2
    else:
        curr_node.next = l1

    return first
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def swapPairs(head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head

    prevNode = head
    node1 = head
    node2 = head.next
    exitNode = node2

    while node2 != None:
        nextNode = node2.next
        prevNode.next = node2
        node2.next = node1
        node1.next = nextNode

        if nextNode == None:
            return exitNode

        prevNode = node1
        node1 = nextNode
        node2 = nextNode.next

    return exitNode

if __name__ == '__main__':

    node_len = 5
    node_list = []
    for i in range(node_len):
        node_list.append(ListNode(i + 1))

    for i in range(node_len - 1):
        node_list[i].next = node_list[i + 1]

    curr_node = swapPairs(node_list[0])

    counter = 0
    while counter < node_len:
        if curr_node != None:
            print(curr_node.val)
            curr_node = curr_node.next
        counter+=1
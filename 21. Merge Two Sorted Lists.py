#Merge two sorted linked lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def intuitive(list1, list2):
    dummy = ListNode()
    curr = dummy
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2
    return dummy.next

def print_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    print(" -> ".join(map(str,vals)))

def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    print_list(list1)
    print_list(list2)
    list3 = (intuitive(list1,list2))
    print_list(list3)

main()
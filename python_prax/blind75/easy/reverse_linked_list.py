class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

def reverse_list(node: ListNode) -> ListNode:
    prev, curr = None, node

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

node = ListNode(10)
node.next = ListNode(20)
node.next.next = ListNode(25)


res = reverse_list(node)
print(res)

# tests = [
#     (43261596, 964176192),
#     (2147483644, 1073741822)
# ]


# for idx, t in enumerate(tests):
#     res = reverse_list(t[0])
#     print(idx, " ", "Test passed" if res == t[1] else "Test Failed")
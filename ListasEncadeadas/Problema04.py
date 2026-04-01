class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def invertList(self, head):
        prev = None
        current = head

        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev

    def removeNodes(self, head):
        head = self.invertList(head)

        current = head
        maxValue = current.val

        while current is not None and current.next is not None:
            if current.next.val < maxValue:
                current.next = current.next.next
            else:
                current = current.next
                maxValue = current.val

        head = self.invertList(head)
        return head

# Teste 1
head1 = ListNode(4)
head1.next = ListNode(1)
head1.next.next = ListNode(6)
head1.next.next.next = ListNode(2)
head1.next.next.next.next = ListNode(5)

result1 = Solution().removeNodes(head1)

while result1:
    print(result1.val, end=" -> ")
    result1 = result1.next
print("None")  # esperado: 6 -> 5 -> None


# Teste 2
head2 = ListNode(2)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(1)
head2.next.next.next.next = ListNode(4)

result2 = Solution().removeNodes(head2)

while result2:
    print(result2.val, end=" -> ")
    result2 = result2.next
print("None")  # esperado: 4 -> None

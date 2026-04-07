class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Detecta o ciclo
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Encontra o início do ciclo
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr

        return None

def create_cycle_list(values, pos):
    """
    values: lista de valores
    pos: índice onde o ciclo começa (-1 se não houver ciclo)
    """
    nodes = [ListNode(v) for v in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]

# Teste 1 (com ciclo)
head1 = create_cycle_list([3, 2, 0, -4], 1)
result1 = sol.detectCycle(head1)
print(result1.val if result1 else None)  # Esperado: 2

# Teste 2 (com ciclo no início)
head2 = create_cycle_list([1, 2], 0)
result2 = sol.detectCycle(head2)
print(result2.val if result2 else None)  # Esperado: 1

# Teste 3 (sem ciclo)
head3 = create_cycle_list([1, 2, 3], -1)
result3 = sol.detectCycle(head3)
print(result3.val if result3 else None)  # Esperado: None

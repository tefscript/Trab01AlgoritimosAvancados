class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        lento = head
        rapido = head
        while rapido and rapido.next:
            lento = lento.next
            rapido = rapido.next.next
        return lento

# --- TESTES NO VSCODE ---
def criar_lista(arr):
    if not arr: return None
    head = ListNode(arr[0])
    atual = head
    for val in arr[1:]:
        atual.next = ListNode(val)
        atual = atual.next
    return head

if __name__ == "__main__":
    sol = Solution()
    
    # Teste 1: Ímpar [1,2,3,4,5]
    lista1 = criar_lista([1, 2, 3, 4, 5])
    print(f"Teste 1 (Meio de 5): {sol.middleNode(lista1).val}")  # Esperado: 3
    
    # Teste 2: Par [1,2]
    lista2 = criar_lista([1, 2])
    print(f"Teste 2 (Meio de 2): {sol.middleNode(lista2).val}")  # Esperado: 2
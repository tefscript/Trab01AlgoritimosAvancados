### Intecalção entre Listas Encadeadas

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        atual = list1
        pos = 0

        # encontrar o nó antes de a
        while pos < a - 1:
            atual = atual.next
            pos += 1

        antes_de_a = atual

        # encontrar o nó depois de b
        while pos < b:
            atual = atual.next
            pos += 1

        depois_de_b = atual.next

        # ligar antes_de_a ao começo da list2
        antes_de_a.next = list2

        # ir até o final da list2
        while list2.next:
            list2 = list2.next

        # ligar final da list2 ao depois_de_b
        list2.next = depois_de_b

        return list1


def criar_lista(valores):
    if len(valores) == 0:
        return None

    head = ListNode(valores[0])
    atual = head

    for i in range(1, len(valores)):
        atual.next = ListNode(valores[i])
        atual = atual.next

    return head


def mostrar_lista(head):
    resultado = []

    while head:
        resultado.append(head.val)
        head = head.next

    return resultado


s = Solution()

# teste 1
list1 = criar_lista([10, 1, 13, 6, 9, 5])
list2 = criar_lista([1000000, 1000001, 1000002])

resultado = s.mergeInBetween(list1, 3, 4, list2)
print("Teste 1:", mostrar_lista(resultado))
print("Esperado: [10, 1, 13, 1000000, 1000001, 1000002, 5]")
print()

# teste 2
list1 = criar_lista([0, 1, 2, 3, 4, 5, 6])
list2 = criar_lista([1000000, 1000001, 1000002, 1000003, 1000004])

resultado = s.mergeInBetween(list1, 2, 5, list2)
print("Teste 2:", mostrar_lista(resultado))
print("Esperado: [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]")
print()

# teste 3
list1 = criar_lista([1, 2, 3, 4, 5])
list2 = criar_lista([9, 8])

resultado = s.mergeInBetween(list1, 1, 3, list2)
print("Teste 3:", mostrar_lista(resultado))
print("Esperado: [1, 9, 8, 5]")
print()

# teste 4
list1 = criar_lista([7, 8, 9, 10])
list2 = criar_lista([1])

resultado = s.mergeInBetween(list1, 1, 2, list2)
print("Teste 4:", mostrar_lista(resultado))
print("Esperado: [7, 1, 10]")
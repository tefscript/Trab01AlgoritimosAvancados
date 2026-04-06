class Solution:
    def findTheWinner(self, n, k):
        friends = list(range(1, n + 1))
        index = 0

        while len(friends) > 1:
            index = (index + k - 1) % len(friends)
            friends.pop(index)

        return friends[0]

  # Teste 1
print(sol.findTheWinner(5, 2))  # Esperado: 3

# Teste 2
print(sol.findTheWinner(6, 5))  # Esperado: 1

# Teste 3
print(sol.findTheWinner(1, 1))  # Esperado: 1

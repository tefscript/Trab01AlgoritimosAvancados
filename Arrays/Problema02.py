from collections import defaultdict

class Solution:
    def prefixConnected(self, words, k):
        prefix_count = defaultdict(int)

        for word in words:
            if len(word) >= k:
                prefix = word[:k]
                prefix_count[prefix] += 1

        groups = 0

        for count in prefix_count.values():
            if count >= 2:
                groups += 1

        return groups

  sol = Solution()

# Teste 1
words1 = ["apple", "ape", "april", "banana"]
k1 = 2
print(sol.prefixConnected(words1, k1))  # Esperado: 1 ("ap")

# Teste 2
words2 = ["car", "cat", "dog", "door"]
k2 = 2
print(sol.prefixConnected(words2, k2))  # Esperado: 2 ("ca", "do")

# Teste 3
words3 = ["hi", "hello", "hey", "hola"]
k3 = 1
print(sol.prefixConnected(words3, k3))  # Esperado: 1 ("h")

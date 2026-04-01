### Contagem de palavras com prefixo específico

class Solution:
    def prefixCount(self, words, pref):
        contador = 0

        for palavra in words:
            if palavra.startswith(pref):
                contador += 1

        return contador


s = Solution()

teste1 = ["pay", "attention", "practice", "attend"]
pref1 = "at"
print("Teste 1:", s.prefixCount(teste1, pref1))
print("Esperado: 2\n")

teste2 = ["leetcode", "win", "loops", "success"]
pref2 = "code"
print("Teste 2:", s.prefixCount(teste2, pref2))
print("Esperado: 0\n")

teste3 = ["apple", "app", "application", "banana"]
pref3 = "app"
print("Teste 3:", s.prefixCount(teste3, pref3))
print("Esperado: 3\n")

teste4 = ["car", "cat", "dog", "cart"]
pref4 = "ca"
print("Teste 4:", s.prefixCount(teste4, pref4))
print("Esperado: 3\n")
### Remover Parênteses Externos

class Solution:
    def removeOuterParentheses(self, s):
        result = ""
        depth = 0

        for c in s:
            if c == '(':
                if depth > 0:
                    result += c
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result += c

        return result


solucao = Solution()

# teste 1 - caso normal
s1 = "(()())(())"
print("Teste 1:", solucao.removeOuterParentheses(s1))
print("Esperado: ()()()")
print()

# teste 2 - caso com mais aninhamento
s2 = "(()())(())(()(()))"
print("Teste 2:", solucao.removeOuterParentheses(s2))
print("Esperado: ()()()()(())")
print()

# teste 3 - caso especial
s3 = "()()"
print("Teste 3:", solucao.removeOuterParentheses(s3))
print("Esperado:")
print()
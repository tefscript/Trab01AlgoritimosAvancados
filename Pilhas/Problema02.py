class Solution(object):
    def removeStars(self, s):
        stack = []

        for i in range(len(s)):
            if s[i] != '*':
                stack.append(s[i])
            else:
                stack.pop()

        result = ""

        for i in range(len(stack)):
            result += stack[i]

        return result

# Teste 1
s1 = "est**rel*as"
print(Solution().removeStars(s1))  # Esperado: "ereas"

# Teste 2
s2 = "remove******"
print(Solution().removeStars(s2))  # Esperado: ""

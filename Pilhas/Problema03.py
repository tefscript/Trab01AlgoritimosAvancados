class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        stack = []
        index_alvo = 0
        
        # 1. Empilha até encontrar o alvo
        for i in range(len(word)):
            stack.append(word[i])
            if word[i] == ch:
                index_alvo = i
                break
        
        # 2. Desempilha para inverter
        prefixo_invertido = ""
        while stack:
            prefixo_invertido += stack.pop()
            
        # 3. Concatena com o restante
        return prefixo_invertido + word[index_alvo + 1:]

# --- TESTES NO VSCODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Teste 1: Alvo no meio
    print(f"Teste 1 (d): {sol.reversePrefix('abcdefd', 'd')}")  # Esperado: dcbaefd
    
    # Teste 2: Alvo não existe
    print(f"Teste 2 (z): {sol.reversePrefix('apple', 'z')}")    # Esperado: apple
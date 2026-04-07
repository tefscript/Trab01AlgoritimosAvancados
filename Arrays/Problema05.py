class Solution:
    def findWinningPlayer(self, skills: list, k: int) -> int:
        n = len(skills)
        if k >= n:
            return skills.index(max(skills))
        
        vencedor_idx = 0
        vitorias = 0
        
        for i in range(1, n):
            if skills[vencedor_idx] > skills[i]:
                vitorias += 1
            else:
                vencedor_idx = i
                vitorias = 1
            
            if vitorias == k:
                return vencedor_idx
        return vencedor_idx

# --- TESTES NO VSCODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Teste 1: Cenário Padrão
    print(f"Teste 1 (k=2): {sol.findWinningPlayer([4, 2, 6, 3, 9], 2)}")  # Esperado: 2
    
    # Teste 2: K muito grande
    print(f"Teste 2 (k=10): {sol.findWinningPlayer([2, 5, 4], 10)}")     # Esperado: 1
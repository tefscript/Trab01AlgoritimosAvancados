class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        listX = []

        for i in range(len(points)):
            listX.append(points[i][0])

        for i in range(len(listX) - 1):
            for j in range(len(listX) - i - 1):
                if listX[j] > listX[j + 1]:
                    temp = listX[j]
                    listX[j] = listX[j + 1]
                    listX[j + 1] = temp

        larger = 0

        for i in range(1, len(listX)):
            dif = listX[i] - listX[i - 1]
            if dif > larger:
                larger = dif

        return larger

# Teste 1
points1 = [[2, 5], [10, 1], [6, 3], [15, 2]]
print(Solution().maxWidthOfVerticalArea(points1))  # esperado: 5

# Teste 2
points2 = [[1, 2], [1, 5], [7, 1], [12, 0]]
print(Solution().maxWidthOfVerticalArea(points2))  # esperado: 6

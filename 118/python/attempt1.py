class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        triangle = [[1]]
        for i in range(1, numRows):
            print("i:", i)
            current = []
            for j in range(i+1):
                print("j:", j)
                if j-1 < 0:
                    left = 0
                else:
                    left = triangle[i-1][j-1]
                print("left:", left)

                if j == i:
                    right = 0
                else:
                    right = triangle[i-1][j]
                print("right:", right)

                current.append(left + right)
                print("current:", current)
            triangle.append(current)
            print("triangle:", triangle)
        
        return triangle
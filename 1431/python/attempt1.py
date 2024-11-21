class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        for i in range(len(candies)):
            candies[i] += extraCandies
            if candies[i] == max(candies):
                results.append(True)
            else:
                results.append(False)
            candies[i] -= extraCandies

        return results
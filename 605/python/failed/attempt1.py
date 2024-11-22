class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            count = 1
            return n <= count

        if len(flowerbed) >= 3:
            for i in range(2, len(flowerbed)):
                # print("flowerbed[i - 2]:", flowerbed[i - 2])
                # print("flowerbed[i - 1]:", flowerbed[i - 1])
                # print("flowerbed[i]:", flowerbed[i])
                if flowerbed[i - 2] == 0 and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i - 1] = 1
                    count += 1
                    # print("CP1")
                    # print("Count:", count)

        # print("flowerbed:", flowerbed)
        # print("flowerbed[0] == 0:", flowerbed[0] == 0)
        # print("flowerbed[1] == 0:", flowerbed[1] == 0)
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] == 1
            count += 1
            # print("CP2")
            # print("Count:", count)

        if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
            flowerbed[len(flowerbed) - 1] = 1
            count += 1
            # print("CP3")
            # print("Count:", count)

        return n <= count
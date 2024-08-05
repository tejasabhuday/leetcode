class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed)-1 or flowerbed[i+1] == 0
            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
    


    # place flowers in alternate pots n = number of flowers to be placed 0 indicates empty pot and 1 = flowered pot
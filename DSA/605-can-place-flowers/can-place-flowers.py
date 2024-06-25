class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i==0 or flowerbed[i-1] == 0:
                    if  i== len(flowerbed)-1 or flowerbed[i+1] == 0:
                        count +=1
                        flowerbed[i] = 1
            if n == count or n< count:
                        return True      
        return False
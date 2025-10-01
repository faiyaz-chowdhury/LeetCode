class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalDrinkableBottles = numBottles
        totalEmptyBottles = numBottles
        # totalDrinkableBottles += numBottles // numExchange
        while True:
            # totalEmptyBottles = (numBottles // numExchange) + (numBottles % numExchange)
            newDrinkableBottles = totalEmptyBottles // numExchange
            totalDrinkableBottles += newDrinkableBottles
            totalEmptyBottles = newDrinkableBottles + (totalEmptyBottles % numExchange)
            if totalEmptyBottles < numExchange:
                return totalDrinkableBottles
            else:
                continue
            
            

        







        

        
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        result = [] 

        maxCandies = 0 

        for numCandy in candies: 
            if numCandy > maxCandies:
                maxCandies = numCandy 

        for kid in candies: 
            if kid + extraCandies >= maxCandies: 
                result.append(True) 
            else:
                result.append(False) 

        return result 


def main(): 
    solution = Solution()
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    result = solution.kidsWithCandies(candies, extraCandies)
    print(result)

if __name__ == "__main__":
    main() 
class Solution(object):
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        shorterLen = min(len(str1), len(str2))

        for i in range(shorterLen, 0, -1):
            if len(str1) % i and len(str2) % i: 
                continue
            
            substring = str1[:i]

            multiple1 = len(str1) // i
            multiple2 = len(str2) // i 

            if substring * multiple1 == str1 and substring * multiple2 == str2: 
                return substring 

        return ""
    
def main(): 
    solution = Solution()
    str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

    result = solution.gcdOfStrings(str1, str2)
    print(result)

if __name__ == "__main__":
    main() 
        
        

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:  
            return ""
    
        
        def gcd(a: int, b:int) -> int:
            while b != 0:
                a,b = b,a%b
            return a

        index = gcd(len(str1), len(str2))
        return str1[:index]


def gcd_iterative(a: int, b: int) -> int:
    while b:
        a, b = b, a%b
    return a


def gcd_recursive(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd_recursive(b, a%b)
    
result = Solution().gcdOfStrings(str1="ABCABC", str2="ABC")
print(result)

print(gcd_recursive(18,11))
from math import sqrt
class Solution:
    def find_factors(self,num):
        result = []
        for i in range(1, num//2 + 1):
            if num%i == 0:
                result.append(i)
        result.append(num)
        return result
    def find_factors_fast(self,num):
        result = []
        rem = 0
        for i in range(1, int(sqrt(num)) + 1):
            if num%i == 0:
                result.append(i)
                if num // i != i:
                    result.append(num // i)
        return result
def main():
    s = Solution()
    number = 36
    result = s.find_factors_fast(number)
    print(f"Factors of number {number} is {result}")

if __name__ == "__main__":
    main()


"""
find_factors
Time complexity O(n/2)
Space complexity O(K)
"""

"""
find_factors_fast
Time complexity O(sqrt(n))
Space complexity O(K)
"""
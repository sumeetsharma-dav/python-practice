"""
# Empty dictionary
d = {}

# With initial key-value pairs
d = {
    "k1": v1,
    "k2": v2,
    "k3": v3
}
"""
class Solution:
    def find_freq(self,x):
        d = {}
        for i in x:
            d[i] = d.get(i,0) + 1
        return d
def main():
    s = Solution()
    list = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,7,8]
    result = s.find_freq(list)
    print(f"Frequency of list {list} is as follow {result}")

if __name__ == "__main__":
    main()
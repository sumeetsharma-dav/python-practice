"""
s="azyxyyzaaaaa"
q=["d","a","y","z"]
"""
class Solution:
    def char_hashing_small(self,s,q):
        char_count = [0] * 26
        for i in range(0, len(s)):
            char_count[(ord(s[i]) - 97)] = char_count[ord(s[i]) - 97] + 1
        for i in q:
            print(f"{i} exists {char_count[(ord(i) - 97)]} times in s")
    def char_hashing_mixed(self,s,q):
        char_count = [0] * 128
        for i in range(0, len(s)):
            char_count[(ord(s[i]))] = char_count[ord(s[i])] + 1
        for i in q:
            print(f"{i} exists {char_count[(ord(i))]} times in s")
def main():
    sol = Solution()
    s="azyxyyzaaaaa"
    s1="azyxyyzaaaaaABBCCCZZZZZ"
    q=["d","a","y","z","x"]
    q1=["d","a","y","z","x","A","B","C","Z"]
    sol.char_hashing_small(s,q)
    sol.char_hashing_mixed(s1,q1)
if __name__ == "__main__":
    main()

"""
TC = O(s+q)
SC = O(i)
"""
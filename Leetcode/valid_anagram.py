class Solution:
    # optimal - sorting
    # t/c: O(n log n), s/c: O(1)
    def isAnagram1(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # optimal - hashtable, my solution
    # t/c: O(n), s/c: O(n)
    def isAnagram2(self, s: str, t: str) -> bool:
        hashtable = {}
        for c in s:
            if c not in hashtable:
                hashtable[c] = 1
            else:
                hashtable[c] += 1
        for c in t:
            if c not in hashtable:
                return False
            else:
                hashtable[c] -= 1
        for key in hashtable:
            if hashtable[key] != 0:
                return False
        return True

    # optimal - hashtable, neetcode solution. same approach but slightly better since two loops instead of three.
    # t/c: O(n), s/c: O(n)
    def isAnagram3(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for key in countS:
            if countS[key] != countT.get(key, 0):
                return False
        return True
    

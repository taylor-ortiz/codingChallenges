class Solution(object):
    def isPalindrome(self, x):
        if x >= 0:
            intArr = [int(i) for i in str(x)]
            intArr.reverse()
            strArr = [str(j) for j in intArr]
            return x == int(''.join(strArr))
        return False
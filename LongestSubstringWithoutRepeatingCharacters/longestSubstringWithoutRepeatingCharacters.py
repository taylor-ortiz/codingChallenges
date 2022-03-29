class Solution(object):
    def lengthOfLongestSubstring(self, s):

        substring = []
        longest = 0
        
        for i in s:
            if (i not in substring):
                substring.append(i)
                if (len(substring) > longest):
                    longest = len(substring)
            else:
                substring = substring[substring.index(i)+1:]
                substring.append(i)        
        return longest
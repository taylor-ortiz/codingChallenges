class Solution:
    def isValid(self, s: str) -> bool:

        # create a mapping of characters in open bracket as key and close as value
        charMapping = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        # generate an empty array
        stack = []
        
        for char in s:
            if charMapping.get(char) != None: # if the map returns something
                # we know its an opening bracket
                stack.append(char)
            else:
                # we know its a closing bracket
                last_value = stack.pop() if stack else '' # get the last open value from stack
                if charMapping.get(last_value, '') != char: # check map, default to '' if not found
                    return False
        return True if not stack else False # ternary for stack array
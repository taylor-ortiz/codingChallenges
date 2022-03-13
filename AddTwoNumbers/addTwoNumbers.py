# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1numb = self.convertNumb(self.lstNodeToArr(l1, []))
    
        l2numb = self.convertNumb(self.lstNodeToArr(l2, []))
        
        return self.arrToListNode([int(i) for i in str(l1numb + l2numb)])
    
    def lstNodeToArr(self, lstNode, finlst):
        if lstNode.next:
            finlst.append(lstNode.val)
            return self.lstNodeToArr(lstNode.next, finlst)
        else:
            finlst.append(lstNode.val)
            finlst.reverse()
            return finlst
    
    def convertNumb(self, lst):
        strings = [str(integer) for integer in lst]
        a_string = "". join(strings)
        return int(a_string)
    
    def arrToListNode(self, numbs):
        nodeList = None
        for x in numbs:
            nodeList = ListNode(x, next=nodeList)
        return nodeList
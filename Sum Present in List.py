"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list 
add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
class testing:
    def __init__(self,list1,num):
        self.l1 = list1 
        self.k = num
        print(l1,k)
    def checkIf(self):
        rest = k
        for i in range(len(l1)):
            check = k - l1[i]
            sub_list = l1[i+1:]
            if(check in l1[:]):
                print(True)
        print(False)


testcase1 = testing([10, 15, 3, 7],17)
testcase1.checkIf()
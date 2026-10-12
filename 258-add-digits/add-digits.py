class Solution(object):
    def addDigits(self, num):
        while num > 9:
            s = 0
            while num > 0:
                s = s + (num % 10)
                num = num // 10
            num = s
        return num

        

        
"""
You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.

Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.
"""

from collections import defaultdict
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = defaultdict(int)
        #n = highLimit - lowLimit + 1
        for num in range(lowLimit,highLimit+1):
            box_no=sum([int(digit) for digit in str(num)])
            box[box_no]+=1

        return max(box.values())

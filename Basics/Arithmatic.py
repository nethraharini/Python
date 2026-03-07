class Solution:
    def totalFine(self, date, car, fine):
        total = 0
        
        for i in range(len(car)):
            if date % 2 == 0:
                if car[i] % 2 != 0:
                    total += fine[i]
            else:
                if car[i] % 2 == 0:
                    total += fine[i]
                    
        return total 


# Given an array of car numbers car[], an array of penalties fine[], and an integer value date. The task is to find the total fine which will be collected on the given date. The fine is collected from odd-numbered cars on even dates and vice versa.

# Examples:

# Input: date = 12, car[] = [2375, 7682, 2325, 2352], fine[] = [250, 500, 350, 200]
# Output: 600
# Explanation: The date is 12 (even), so we collect the fine from odd-numbered cars. The odd-numbered cars and the fines associated with them are as follows:
# 2375 -> 250
# 2325 -> 350
# The sum of the fines is 250+350 = 600

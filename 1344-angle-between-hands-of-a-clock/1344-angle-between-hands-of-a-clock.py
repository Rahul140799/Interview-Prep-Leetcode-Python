class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
            
        total_minutes = hour*60 + minutes
        
        long_hand = minutes*6
        short_hand = total_minutes*(0.5)
        
        return min(360 - abs(long_hand - short_hand), abs(long_hand - short_hand))
        
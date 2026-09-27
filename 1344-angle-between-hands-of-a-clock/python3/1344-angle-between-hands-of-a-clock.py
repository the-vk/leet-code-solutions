class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        DEG_TO_MIN = 6.0
        DEG_TO_HOUR = 30.0
        DEG_TO_HOUR_MIN = 0.5

        hour = hour % 12

        minute_degree = minutes * DEG_TO_MIN
        hours_degree = hour * DEG_TO_HOUR + minutes * DEG_TO_HOUR_MIN

        diff = abs(minute_degree - hours_degree)
        if (diff - 180.0) >= 0.005:
            diff = 360.0 - diff
        
        return diff

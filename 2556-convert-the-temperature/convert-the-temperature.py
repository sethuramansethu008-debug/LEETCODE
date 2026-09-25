class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        k=celsius+273.15
        f=celsius*1.80+32.00
        return k,f
        
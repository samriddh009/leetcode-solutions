class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        cx = max(x1,min(xCenter,x2))
        cy = max(y1,min(yCenter,y2))
        c1 = (cx-xCenter)**2
        c2 = (cy-yCenter)**2
        if c1+c2<=radius**2:
            return True 
        else:
            return False